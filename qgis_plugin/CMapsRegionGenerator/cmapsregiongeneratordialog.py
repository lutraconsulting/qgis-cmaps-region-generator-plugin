# -*- coding: utf-8 -*-

# CMAPS Region Generator - Automate merging features using a CSV file definition.
# Copyright (C) 2013 Centigon Solutions Inc.

# sales at centigonsolutions dot com
# 1333 Camino Del Rio S #300
# San Diego 
# CA 92108
# USA

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_cmapsregiongenerator import Ui_CMapsRegionGenerator
from tableau_writer import *
import about_dialog

import os
from unicode_csv import UnicodeReader
        
# create the dialog for zoom to point


class CMapsRegionGeneratorDialog(QDialog, Ui_CMapsRegionGenerator):
    
    def __init__(self,  iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        self.loadedOK = True

        # Used to keep track of user preferences
        self.preferredStandardGeoCol = 0
        self.yourRegionDefCol = 1

        self.maxFeaturesToCheckForVals = 50
        
        """
            Based on selected Shapefile:
                Read all attribute names
                    Take an example (first non-zero-length)
                Populate combo-box
        """
        
        if self.iface.mapCanvas().currentLayer() == None or \
           self.iface.mapCanvas().currentLayer().type() != QgsMapLayer.VectorLayer:
            # Show QMessageBox (error) and close
            QMessageBox.critical(self, 'Error', 'Please first select an input Shapefile.')
            self.loadedOK = False
            return
        self.inputLayer = self.iface.mapCanvas().currentLayer()
        
        # Display the CRS
        self.srsCrs = self.inputLayer.crs()
        crsDesc = str( self.srsCrs.description() )
        
        self.selectedCrsLabel.setText( 'Input CRS: %s (Output will always be in WGS 84)' % (crsDesc,) )
        
        # Fetch the attribute names
        try:
            for index, field in self.inputLayer.dataProvider().fields().iteritems():
                # Get sample
                sampleText = self.getSample(index)
                if sampleText is not None:
                    self.mergingAttributeComboBox.addItem( '%s (e.g. %s)' % (field.name(), sampleText) )
                else:
                    self.mergingAttributeComboBox.addItem( '%s' % (field.name(),) )
        except:
            i = 0
            for field in self.inputLayer.dataProvider().fields():
                # Get sample
                sampleText = self.getSample(i)
                if sampleText is not None:
                    self.mergingAttributeComboBox.addItem( '%s (e.g. %s)' % (field.name(), sampleText) )
                else:
                    self.mergingAttributeComboBox.addItem( '%s' % (field.name(),) )
                i += 1
        

    def getSample(self, attributeIndex):
        # Fetch the value (as a string) of the first attribute
        f = QgsFeature()
        for indexToTry in xrange( min(self.inputLayer.featureCount(), self.maxFeaturesToCheckForVals) ):
            try:
                self.inputLayer.featureAtId(indexToTry, f, False, True)
                stringVal = str( f.attributeMap()[attributeIndex].toString() )
                if len(stringVal) > 0:
                    return stringVal
            except:
                self.inputLayer.dataProvider().getFeatures(QgsFeatureRequest(indexToTry)).nextFeature(f)
                stringVal = str( f.attributes()[attributeIndex] )
                if len(stringVal) > 0:
                    return stringVal
        return None


    def updateCsvCombos(self, csvFilePath):
        """

        Updates the two combo boxes with samples from the CSV file

        :param csvFilePath: Path to CSV file, file may not be valid
        :return:
        """

        # Clear the combo boxes
        self.standardGeographyColumnComboBox.blockSignals(True)
        self.yourRegionDefinitionColumnComboBox.blockSignals(True)
        self.standardGeographyColumnComboBox.clear()
        self.yourRegionDefinitionColumnComboBox.clear()
        self.standardGeographyColumnComboBox.blockSignals(False)
        self.yourRegionDefinitionColumnComboBox.blockSignals(False)

        # Determine if the file is valid and return early if not, leaving the combo boxes empty
        try:
            if csvFilePath.startswith('"') and csvFilePath.endswith('"'):
                csvFilePath = csvFilePath[1:-1]
            with open(csvFilePath, 'rb') as csvFile:
                reader = UnicodeReader(csvFile)
                firstRow = reader.next()
                if len(firstRow) < 2:
                    # There should be at least two columns, return
                    return
                # populate the CBs
                i = 1
                self.standardGeographyColumnComboBox.blockSignals(True)
                self.yourRegionDefinitionColumnComboBox.blockSignals(True)
                for col in firstRow:
                    cbText = 'Column %d (e.g. %s)' % (i, col)
                    self.standardGeographyColumnComboBox.addItem(cbText)
                    self.yourRegionDefinitionColumnComboBox.addItem(cbText)
                    i += 1
                self.standardGeographyColumnComboBox.setCurrentIndex(self.preferredStandardGeoCol)
                self.yourRegionDefinitionColumnComboBox.setCurrentIndex(self.yourRegionDefCol)
                self.standardGeographyColumnComboBox.blockSignals(False)
                self.yourRegionDefinitionColumnComboBox.blockSignals(False)
        except IOError:
            # The user could be typing and we have a partial file name
            pass

    def colNumFromComboText(self, comboText):
        return int( comboText.split('Column ')[1].split(' ')[0] )

    def onStandardGeogColChanged(self, newVal):
        # User updated the combo box, record the preference
        self.preferredStandardGeoCol = self.colNumFromComboText(newVal) - 1

    def onYourRegionDefColChanged(self, newVal):
        # User updated the combo box, record the preference
        self.yourRegionDefCol = self.colNumFromComboText(newVal) - 1

    def run(self):
        """
            The guts of the plugin
            
            Overview:
                Determine the unique entries in the SUB_REGION column
                For each unique entry:
                    Make a list of all the matching entries from the STATE_NAME column
                    Select all features whose attributes match this string
                    Merge the features
                    Add STATE_NAME as a new column
                    Write to output file
                Optionally load the layer
        """
        
        """
            Before starting, check the quality of the input data. The 
            regions that we are merging should not have any invalid 
            geometries as these cause major problems later on.
        """
        
        prov = self.inputLayer.dataProvider()
        allFeatures = []
        errorString = ''
        feat = QgsFeature()
        if QGis.QGIS_VERSION_INT >= 20000:
            featIt = prov.getFeatures()
            while featIt.nextFeature(feat):
                allFeatures.append(QgsFeature(feat)) ## Append a copy
        else:
            prov.select(prov.attributeIndexes())
            while prov.nextFeature(feat):
                allFeatures.append(QgsFeature(feat)) ## Append a copy
        for feat in allFeatures:
            if not feat.geometry().isGeosValid():
                # Determine what's wrong with it
                errorString += '\n\n'
                errorString += 'Feature %d has the following error(s):\n\n' % feat.id()
                for res in feat.geometry().validateGeometry():
                    errorString += res.what() + '\n'
        if len(errorString) > 0:
            QMessageBox.critical(self, 'Invalid Geometry Detected', 'The following geometry errors were detected and must be resolved before generating regions:' + errorString)
            return
        
        """
            Prepare the output file
            
            Check first that a layer with the same file name is not 
            already loaded.  If it is, raise an error and return early.
        """
        
        targetSrs = QgsCoordinateReferenceSystem(4326)
        crsTransform = QgsCoordinateTransform(self.srsCrs, targetSrs)
        
        outputFolder = self.outputFolderLineEdit.text()
        if outputFolder == '':
            QMessageBox.critical(self, 'Error', 'No output folder specified.')
            return
        # Ensure the output folder exists
        if not os.path.isdir(outputFolder):
            try:
                os.makedirs(outputFolder)
            except WindowsError:
                QMessageBox.critical(self, 'Error', 'Failed to make destination folder, %s' % (outputFolder))
                return

        outputFilePrefix = self.outputFilePrefixLineEdit.text()
        if outputFilePrefix == '':
            QMessageBox.critical(self, 'Error', 'No output file prefix specified.')
            return

        shapeFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '.shp'))
        geoJsonFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '.geojson'))
        geoJsonKeylessFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '_no_keys.geojson'))
        csvFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '.csv'))
        tableauFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '_tableau.csv'))
        lr = QgsMapLayerRegistry.instance()
        for of in [shapeFileName, geoJsonFileName, geoJsonKeylessFileName, csvFileName]:
            shortName = os.path.basename(of).split('.')[0]
            for layer in lr.mapLayers().values():
                if layer.type() == QgsMapLayer.VectorLayer and os.path.normpath(str(layer.source())) == of:
                    # The file we are trying to write is already open
                    QMessageBox.critical(self, 'Error', 'The file you\'re trying to write (%s) is already loaded, please close it first.' % (layer.name()))
                    return
        
        fields = None
        if QGis.QGIS_VERSION_INT >= 20000:
            fields = QgsFields()
            fields.append( QgsField("region", QVariant.String) )
        else:
            fields = { 0 : QgsField("region", QVariant.String) }
        emptyFields = QgsFields()

        encoding = 'utf-8'

        shapeWriter = QgsVectorFileWriter(shapeFileName, encoding, fields, QGis.WKBPolygon, targetSrs, 'ESRI Shapefile')
        if shapeWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.critical(self, 'Error', 'Failed to create output file %s' % (shapeFileName))
            return
        geoJsonWriter = QgsVectorFileWriter(geoJsonFileName, encoding, fields, QGis.WKBPolygon, targetSrs, 'GeoJSON',
                                            layerOptions=['COORDINATE_PRECISION=5'])
        if geoJsonWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.critical(self, 'Error', 'Failed to create output file %s' % (geoJsonFileName))
            return
        geoJsonKeylessWriter = QgsVectorFileWriter(geoJsonKeylessFileName, encoding, emptyFields, QGis.WKBPolygon, targetSrs,
                                                   'GeoJSON', layerOptions=['COORDINATE_PRECISION=5'])
        if geoJsonKeylessWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.critical(self, 'Error', 'Failed to create output file %s' % (geoJsonKeylessFileName))
            return
        csvWriter = QgsVectorFileWriter(csvFileName, encoding, fields, QGis.WKBPolygon, targetSrs, 'CSV',
                                        layerOptions=['GEOMETRY=AS_WKT'])
        if csvWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.critical(self, 'Error', 'Failed to create output file %s' % (csvFileName))
            return
        while True:
            try:
                tableauWriter = TableauWriter(tableauFileName, fields)
                break
            except TableauFileCreationError:
                reply = QMessageBox.question(None, 'File in Use',
                                                   '%s appears to already be open in another application. Please either close '
                                                   'the file and retry or click Abort to cancel.' % tableauFileName,
                                                   QMessageBox.Retry | QMessageBox.Abort, QMessageBox.Retry)
                if reply == QMessageBox.Abort:
                    return

        # Read CSV control file
        uniqueRegionIds = {} # A dict
        csvFileH = open( str(self.regionDefinitionFileNameLineEdit.text()), 'rb')
        reader = UnicodeReader(csvFileH)
        if self.firstRowIsHeaderCheckBox.isChecked():
            # Eat header
            reader.next()
        standardGeogColIdx = self.standardGeographyColumnComboBox.currentIndex()
        yourRegionDefColIdx = self.yourRegionDefinitionColumnComboBox.currentIndex()
        for row in reader:
            fips = row[standardGeogColIdx]
            regionId = row[yourRegionDefColIdx]
            if not regionId in uniqueRegionIds.keys():
                uniqueRegionIds[regionId] = { 'subregion_names': [fips],
                                              'matched_subregion_names': [] }
            else:
                uniqueRegionIds[regionId]['subregion_names'].append(fips)
        del reader
        csvFileH.close()
        
        # Determine index of merging attribute
        attIdx = self.mergingAttributeComboBox.currentIndex()
        
        feat = QgsFeature()
        prov = self.inputLayer.dataProvider()
        allAttrs = prov.attributeIndexes()
        hasMismatches = False
        mismatchReport = 'Custom Region,Unmatched Subregions\n'  # Header
        for region, subRegionInfo in uniqueRegionIds.iteritems():
            subRegions = subRegionInfo['subregion_names']
            # Make a selection of features
            matchedFeatures = []
            if QGis.QGIS_VERSION_INT >= 20000:
                featIt = prov.getFeatures()
                while featIt.nextFeature(feat):
                    subRegionName = str(feat.attributes()[attIdx])
                    if subRegionName in subRegions:
                        matchedFeatures.append(QgsFeature(feat)) ## Append a copy
                        subRegionInfo['matched_subregion_names'].append(subRegionName)
            else:
                prov.select(allAttrs)
                while prov.nextFeature(feat):
                    subRegionName = str(feat.attributeMap()[attIdx].toString())
                    if subRegionName in subRegions:
                        matchedFeatures.append(QgsFeature(feat)) ## Append a copy
                        subRegionInfo['matched_subregion_names'].append(subRegionName)
            # matchedFeatures should now contain all we require to merge
            # if it has no entries, then no features could be found with this 
            # sub-region attribute so it will be skipped and not appear in the 
            # output.  
            if len(matchedFeatures) < len(subRegionInfo['subregion_names']):
                # There are more subregions in the definition than have actually been matched
                # so the output geometry is likely to have weird holes. Add this information to the
                # mismatch report
                hasMismatches = True
                mismatchReport += '%s\n' % region
                for subregion in subRegionInfo['subregion_names']:
                    if subregion not in subRegionInfo['matched_subregion_names']:
                        mismatchReport += ',%s\n' % subregion

            if len(matchedFeatures) == 0:
                continue

            firstFeature = matchedFeatures.pop()
            mergedGeom = QgsGeometry( firstFeature.geometry() )
            for featureToMerge in matchedFeatures:
                mergedGeom = mergedGeom.combine(featureToMerge.geometry())
            # We now should have a merged geometry
            # Transform to 4326
            if mergedGeom.transform(crsTransform) != 0:
                QMessageBox.critical(self, 'Error', 'Failed to perform CRS transform, quitting.')
                del shapeWriter
                del geoJsonWriter
                del geoJsonKeylessWriter
                del csvWriter
                return
            if QGis.QGIS_VERSION_INT >= 20000:
                outFet = QgsFeature(fields)
                outFet.setGeometry(mergedGeom)
                outFet.setAttribute('region', region)
                keylessFeat = QgsFeature(emptyFields)
                keylessFeat.setGeometry(mergedGeom)
            else:
                outFet = QgsFeature()
                outFet.setGeometry(mergedGeom)
                outFet.addAttribute(0, QVariant(region))
                keylessFeat = QgsFeature()
                keylessFeat.setGeometry(mergedGeom)
            shapeWriter.addFeature(outFet)
            geoJsonWriter.addFeature(outFet)
            geoJsonKeylessWriter.addFeature(keylessFeat)
            csvWriter.addFeature(outFet)
            tableauWriter.addFeature(outFet)
        # close output file
        del shapeWriter
        del geoJsonWriter
        del geoJsonKeylessWriter
        del csvWriter

        if tableauWriter.encounteredHoles():
            holeFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '_holes.csv'))
            while True:
                try:
                    hFile = open(holeFileName, 'w')
                    break
                except:
                    reply = QMessageBox.question(None, 'File in Use',
                                                 '%s appears to already be open in another application. Please either close '
                                                 'the file and retry or click Abort to cancel.' % holeFileName,
                                                 QMessageBox.Retry | QMessageBox.Abort, QMessageBox.Retry)
                    if reply == QMessageBox.Abort:
                        return
            hFile.write(tableauWriter.getHoleSummary())
            hFile.close()

        if hasMismatches:
            mismatchFileName = os.path.normpath(os.path.join(outputFolder, outputFilePrefix + '_mismatches.csv'))
            while True:
                try:
                    mmFile = open(mismatchFileName, 'w')
                    break
                except:
                    reply = QMessageBox.question(None, 'File in Use',
                                                 '%s appears to already be open in another application. Please either close '
                                                 'the file and retry or click Abort to cancel.' % mismatchFileName,
                                                 QMessageBox.Retry | QMessageBox.Abort, QMessageBox.Retry)
                    if reply == QMessageBox.Abort:
                        return

            mmFile.write(mismatchReport)
            mmFile.close()

        if hasMismatches or tableauWriter.encounteredHoles():
            issuesMessage = 'The following issues were encountered while exporting:'
            if hasMismatches:
                issuesMessage += '\n\nFailed to locate matching input sub-regions for some of your custom region definitions.' \
                                 ' Please see %s for more details.' % mismatchFileName
            if tableauWriter.encounteredHoles():
                issuesMessage += '\n\nSome of your custom regions contained holes / inner rings which are not supported by ' \
                                 'the tableau file format. Holes / inner rings of the affected regions have not been written ' \
                                 'to the exported tableau file. ' \
                                 'Please see %s for more details.' % holeFileName
            QMessageBox.warning(self, 'Export Issues', issuesMessage)

        del tableauWriter

        # Optionally load the layer in QGIS
        if self.loadWhenFinishedCheckBox.isChecked():
            for of in [shapeFileName, geoJsonFileName, geoJsonKeylessFileName, csvFileName]:
                shortName = os.path.basename(of)
                loadedLayer = QgsVectorLayer(of, shortName, 'ogr')
                if not loadedLayer.isValid():
                    QMessageBox.critical(self, 'Error', 'Failed to load resulting shapefile %s.' % (of))
                    return
                QgsMapLayerRegistry.instance().addMapLayer(loadedLayer)
        
        QMessageBox.information(self, 'Success', 'Successfully finished processing.')
    
        
    def showHelp(self):
        QDesktopServices.openUrl(QUrl(QString('http://centigonknowledge.com/cmaps-analytics-region-creator')))
    
    
    def aboutClicked(self):
        d = about_dialog.AboutDialog(self.iface)
        d.show()
        res = d.exec_()
    
    
    def browseForRegion(self):
        """
            User is browsing for a region definition:
            
                Check that the file is a .csv file
                Open it and read the column titles
                
        """
        
        # Remember the last folder in which we searched
        settings = QSettings()
        try:
            lastFolder = str(settings.value("cmapsregiongenerator/lastRegionFolder", os.sep).toString())
        except:
            lastFolder = str(settings.value("cmapsregiongenerator/lastRegionFolder", os.sep))
        
        tmpFileName = str( QFileDialog.getOpenFileName(self, 'Select Region Definition', lastFolder, 'Comma Separated Variable Files (*.csv)') )
        if not len(tmpFileName) > 0 or not os.path.exists(tmpFileName):
            QMessageBox.critical(self, 'Error', tmpFileName + ' does not seem to exist.')
            return
        
        # Store the path we just looked in
        head, tail = os.path.split(tmpFileName)
        if head <> os.sep and head.lower() <> 'c:\\' and head <> '':
            settings.setValue("cmapsregiongenerator/lastRegionFolder", head)
        
        self.regionDefinitionFileNameLineEdit.setText( tmpFileName )
        
    
    def browseForShapefile(self):
        
        # Remember the last folder in which we searched
        settings = QSettings()
        try:
            lastFolder = str(settings.value("cmapsregiongenerator/lastShapefileFolder", os.sep).toString())
        except:
            lastFolder = str(settings.value("cmapsregiongenerator/lastShapefileFolder", os.sep))
        
        tmpFolderName = str( QFileDialog.getExistingDirectory(self, 'Select Output Folder', lastFolder) )
        
        # Store the path we just looked in
        if tmpFolderName != '':
            settings.setValue("cmapsregiongenerator/lastShapefileFolder", tmpFolderName)
        
        self.outputFolderLineEdit.setText( tmpFolderName )
