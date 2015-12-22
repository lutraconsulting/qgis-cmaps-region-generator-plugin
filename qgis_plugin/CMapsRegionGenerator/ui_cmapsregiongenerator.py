# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cmapsregiongenerator.ui'
#
# Created: Tue Dec 22 11:35:55 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CMapsRegionGenerator(object):
    def setupUi(self, CMapsRegionGenerator):
        CMapsRegionGenerator.setObjectName(_fromUtf8("CMapsRegionGenerator"))
        CMapsRegionGenerator.setWindowModality(QtCore.Qt.ApplicationModal)
        CMapsRegionGenerator.resize(550, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cmapsregiongenerator/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CMapsRegionGenerator.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(CMapsRegionGenerator)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.typeLabel = QtGui.QLabel(CMapsRegionGenerator)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.gridLayout.addWidget(self.typeLabel, 0, 0, 1, 1)
        self.selectedCrsLabel = QtGui.QLabel(CMapsRegionGenerator)
        self.selectedCrsLabel.setObjectName(_fromUtf8("selectedCrsLabel"))
        self.gridLayout.addWidget(self.selectedCrsLabel, 1, 0, 1, 3)
        self.selectedCrsLabel_2 = QtGui.QLabel(CMapsRegionGenerator)
        self.selectedCrsLabel_2.setObjectName(_fromUtf8("selectedCrsLabel_2"))
        self.gridLayout.addWidget(self.selectedCrsLabel_2, 2, 0, 1, 1)
        self.mergingAttributeComboBox = QtGui.QComboBox(CMapsRegionGenerator)
        self.mergingAttributeComboBox.setObjectName(_fromUtf8("mergingAttributeComboBox"))
        self.gridLayout.addWidget(self.mergingAttributeComboBox, 3, 0, 1, 1)
        self.selectedCrsLabel_3 = QtGui.QLabel(CMapsRegionGenerator)
        self.selectedCrsLabel_3.setObjectName(_fromUtf8("selectedCrsLabel_3"))
        self.gridLayout.addWidget(self.selectedCrsLabel_3, 4, 0, 1, 1)
        self.regionDefinitionFileNameLineEdit = QtGui.QLineEdit(CMapsRegionGenerator)
        self.regionDefinitionFileNameLineEdit.setObjectName(_fromUtf8("regionDefinitionFileNameLineEdit"))
        self.gridLayout.addWidget(self.regionDefinitionFileNameLineEdit, 5, 0, 1, 2)
        self.browseRegionDefinitionPushButton = QtGui.QPushButton(CMapsRegionGenerator)
        self.browseRegionDefinitionPushButton.setToolTip(_fromUtf8(""))
        self.browseRegionDefinitionPushButton.setObjectName(_fromUtf8("browseRegionDefinitionPushButton"))
        self.gridLayout.addWidget(self.browseRegionDefinitionPushButton, 5, 2, 1, 1)
        self.firstRowIsHeaderCheckBox = QtGui.QCheckBox(CMapsRegionGenerator)
        self.firstRowIsHeaderCheckBox.setChecked(True)
        self.firstRowIsHeaderCheckBox.setObjectName(_fromUtf8("firstRowIsHeaderCheckBox"))
        self.gridLayout.addWidget(self.firstRowIsHeaderCheckBox, 6, 0, 1, 1)
        self.standardGeographyColumnLabel = QtGui.QLabel(CMapsRegionGenerator)
        self.standardGeographyColumnLabel.setObjectName(_fromUtf8("standardGeographyColumnLabel"))
        self.gridLayout.addWidget(self.standardGeographyColumnLabel, 7, 0, 1, 1)
        self.standardGeographyColumnComboBox = QtGui.QComboBox(CMapsRegionGenerator)
        self.standardGeographyColumnComboBox.setObjectName(_fromUtf8("standardGeographyColumnComboBox"))
        self.gridLayout.addWidget(self.standardGeographyColumnComboBox, 7, 1, 1, 2)
        self.label = QtGui.QLabel(CMapsRegionGenerator)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.yourRegionDefinitionColumnComboBox = QtGui.QComboBox(CMapsRegionGenerator)
        self.yourRegionDefinitionColumnComboBox.setObjectName(_fromUtf8("yourRegionDefinitionColumnComboBox"))
        self.gridLayout.addWidget(self.yourRegionDefinitionColumnComboBox, 8, 1, 1, 2)
        self.selectedCrsLabel_4 = QtGui.QLabel(CMapsRegionGenerator)
        self.selectedCrsLabel_4.setObjectName(_fromUtf8("selectedCrsLabel_4"))
        self.gridLayout.addWidget(self.selectedCrsLabel_4, 9, 0, 1, 1)
        self.loadWhenFinishedCheckBox = QtGui.QCheckBox(CMapsRegionGenerator)
        self.loadWhenFinishedCheckBox.setChecked(True)
        self.loadWhenFinishedCheckBox.setObjectName(_fromUtf8("loadWhenFinishedCheckBox"))
        self.gridLayout.addWidget(self.loadWhenFinishedCheckBox, 12, 0, 1, 2)
        self.label_2 = QtGui.QLabel(CMapsRegionGenerator)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)
        self.outputFilePrefixLineEdit = QtGui.QLineEdit(CMapsRegionGenerator)
        self.outputFilePrefixLineEdit.setObjectName(_fromUtf8("outputFilePrefixLineEdit"))
        self.gridLayout.addWidget(self.outputFilePrefixLineEdit, 11, 1, 1, 1)
        self.outputFolderLineEdit = QtGui.QLineEdit(CMapsRegionGenerator)
        self.outputFolderLineEdit.setObjectName(_fromUtf8("outputFolderLineEdit"))
        self.gridLayout.addWidget(self.outputFolderLineEdit, 9, 1, 1, 1)
        self.browseNewShapefilePushButton = QtGui.QPushButton(CMapsRegionGenerator)
        self.browseNewShapefilePushButton.setToolTip(_fromUtf8(""))
        self.browseNewShapefilePushButton.setObjectName(_fromUtf8("browseNewShapefilePushButton"))
        self.gridLayout.addWidget(self.browseNewShapefilePushButton, 9, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 212, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aboutPushButton = QtGui.QPushButton(CMapsRegionGenerator)
        self.aboutPushButton.setObjectName(_fromUtf8("aboutPushButton"))
        self.horizontalLayout.addWidget(self.aboutPushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(CMapsRegionGenerator)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(CMapsRegionGenerator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CMapsRegionGenerator.run)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CMapsRegionGenerator.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("helpRequested()")), CMapsRegionGenerator.showHelp)
        QtCore.QObject.connect(self.aboutPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CMapsRegionGenerator.aboutClicked)
        QtCore.QObject.connect(self.browseRegionDefinitionPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CMapsRegionGenerator.browseForRegion)
        QtCore.QObject.connect(self.browseNewShapefilePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CMapsRegionGenerator.browseForShapefile)
        QtCore.QObject.connect(self.regionDefinitionFileNameLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), CMapsRegionGenerator.updateCsvCombos)
        QtCore.QObject.connect(self.yourRegionDefinitionColumnComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), CMapsRegionGenerator.onYourRegionDefColChanged)
        QtCore.QObject.connect(self.standardGeographyColumnComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), CMapsRegionGenerator.onStandardGeogColChanged)
        QtCore.QMetaObject.connectSlotsByName(CMapsRegionGenerator)

    def retranslateUi(self, CMapsRegionGenerator):
        CMapsRegionGenerator.setWindowTitle(_translate("CMapsRegionGenerator", "CMaps Region Generator", None))
        self.typeLabel.setText(_translate("CMapsRegionGenerator", "Type: ESRI Shapefile", None))
        self.selectedCrsLabel.setText(_translate("CMapsRegionGenerator", "Input CRS: WGS 84 (Output will always be in WGS 84)", None))
        self.selectedCrsLabel_2.setToolTip(_translate("CMapsRegionGenerator", "Location identifier that matches a column contained in your region definition CSV file.", None))
        self.selectedCrsLabel_2.setText(_translate("CMapsRegionGenerator", "Shapefile Attribute for Merging", None))
        self.mergingAttributeComboBox.setToolTip(_translate("CMapsRegionGenerator", "Location identifier that matches a column contained in your region definition CSV file.", None))
        self.selectedCrsLabel_3.setToolTip(_translate("CMapsRegionGenerator", "CSV file that contains 2 columns of data. The first column contains your custom regions / territories. The second column should contain the same Shapefile Attribute for Merging from your original Shapefile.", None))
        self.selectedCrsLabel_3.setText(_translate("CMapsRegionGenerator", "Region Definition (.CSV file)", None))
        self.regionDefinitionFileNameLineEdit.setToolTip(_translate("CMapsRegionGenerator", "CSV file that contains 2 columns of data. The first column contains your custom regions / territories. The second column should contain the same Shapefile Attribute for Merging from your original Shapefile.", None))
        self.browseRegionDefinitionPushButton.setText(_translate("CMapsRegionGenerator", "Browse", None))
        self.firstRowIsHeaderCheckBox.setToolTip(_translate("CMapsRegionGenerator", "Leave this option checked if the Region Definition file contains column titles. This will force the generator to ignore the first row. Uncheck if the CSV file does NOT contain column titles.", None))
        self.firstRowIsHeaderCheckBox.setText(_translate("CMapsRegionGenerator", "First Row Contains Column Titles", None))
        self.standardGeographyColumnLabel.setToolTip(_translate("CMapsRegionGenerator", "Values that correspond to the Shapefile Attribute selected that will be merged according to the Region Definition Column (default is column 1).", None))
        self.standardGeographyColumnLabel.setText(_translate("CMapsRegionGenerator", "Standard Geography Column", None))
        self.standardGeographyColumnComboBox.setToolTip(_translate("CMapsRegionGenerator", "Values that correspond to the Shapefile Attribute selected that will be merged according to the Region Definition Column (default is column 1).", None))
        self.label.setToolTip(_translate("CMapsRegionGenerator", "List of new unique regions to be output in the new boundary file. (default is column 2).", None))
        self.label.setText(_translate("CMapsRegionGenerator", "Your Region Definition Column", None))
        self.yourRegionDefinitionColumnComboBox.setToolTip(_translate("CMapsRegionGenerator", "List of new unique regions to be output in the new boundary file. (default is column 2).", None))
        self.selectedCrsLabel_4.setToolTip(_translate("CMapsRegionGenerator", "Directory where the new region files will be saved.", None))
        self.selectedCrsLabel_4.setText(_translate("CMapsRegionGenerator", "Save New Region File Output to", None))
        self.loadWhenFinishedCheckBox.setText(_translate("CMapsRegionGenerator", "Load into canvas when finished", None))
        self.label_2.setToolTip(_translate("CMapsRegionGenerator", "Prefix used to name output files.", None))
        self.label_2.setText(_translate("CMapsRegionGenerator", "Output File Prefix", None))
        self.outputFilePrefixLineEdit.setToolTip(_translate("CMapsRegionGenerator", "Prefix used to name output files.", None))
        self.outputFolderLineEdit.setToolTip(_translate("CMapsRegionGenerator", "Directory where the new region files will be saved.", None))
        self.browseNewShapefilePushButton.setText(_translate("CMapsRegionGenerator", "Browse", None))
        self.aboutPushButton.setText(_translate("CMapsRegionGenerator", "About", None))

import resources_rc
