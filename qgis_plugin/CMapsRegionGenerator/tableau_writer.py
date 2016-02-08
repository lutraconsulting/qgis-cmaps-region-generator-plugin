from qgis.core import QGis
from unicode_csv import UnicodeWriter


class TableauFileCreationError(Exception):

    def __init__(self, msg=''):
        Exception.__init__(self,msg)


class TableauUnexpectedGeometryTypeError(Exception):

    def __init__(self, msg=''):
        Exception.__init__(self,msg)


class TableauGeometryError(Exception):

    def __init__(self, msg=''):
        Exception.__init__(self,msg)


class TableauWriter():

    def __init__(self, fileName, fields):
        """

        :param fileName:    String, output file
        :param fields:      QgsFields, the layer's fields
        :return:
        """
        self.fileName = fileName
        self.fields = fields
        self.regionsWithHoles = []
        self.nextFeatureId = 1
        try:
            self.file = open(self.fileName, 'wb')
        except IOError:
            raise TableauFileCreationError()
        self.writer = UnicodeWriter(self.file)
        self._writeHeader()

    def __del__(self):
        """
        Gracefully closes the ouput file
        :return:
        """
        self.file.close()

    def _writeHeader(self):
        """
        Writes the header
        :return:
        """
        fieldNames = []
        for field in self.fields:
            fieldNames.append(field.name())
        header = ['PolygonID']
        header.extend(fieldNames)
        header.extend(['SubPolygonID', 'PointID', 'Longitude', 'Latitude'])
        self.writer.writerow(header)

    def _getNextFeatureId(self):
        nextFeatureId = self.nextFeatureId
        self.nextFeatureId += 1
        return nextFeatureId

    def addFeature(self, feature):
        """
        :param feature:
        :return:
        """
        idAndFields = []
        # Feature ID
        idAndFields.append(self._getNextFeatureId())
        # fields
        for field in self.fields:
            idAndFields.append(feature[field.name()])

        # Geometry
        if feature.geometry().wkbType() == QGis.WKBPolygon:
            poly = feature.geometry().asPolygon()
            self._writePolygon(idAndFields, 1, poly)
            if len(poly) > 1:
                if feature['region'] not in self.regionsWithHoles:
                    self.regionsWithHoles.append(feature['region'])
        elif feature.geometry().wkbType() == QGis.WKBMultiPolygon:
            polys = feature.geometry().asMultiPolygon()
            partNo = 1
            for poly in polys:
                self._writePolygon(idAndFields, partNo, poly)
                partNo += 1
                if len(poly) > 1:
                    if feature['region'] not in self.regionsWithHoles:
                        self.regionsWithHoles.append(feature['region'])
        else:
            raise TableauUnexpectedGeometryTypeError()

    def encounteredHoles(self):
        """
        Reports whether or not we wrote any geometry that had holes
        :return:    Boolean - whether we encountered geometry with holes while exporting
        """
        return len(self.regionsWithHoles) > 0

    def getHoleSummary(self):
        """
        Produces summary content for a CSV file for user to identify regions having holes
        :return:    String - content for a CSV file describing the problem regions
        """
        reportString = ''
        reportString += 'Regions With Holes\n'
        for regionWithHole in self.regionsWithHoles:
            reportString += '%s\n' % regionWithHole
        return reportString

    def _writePolygon(self, idAndFields, subPolygonId, poly):
        if len(poly) < 1:
            raise TableauGeometryError('Polygon had 0 rings')
        pointId = 1
        # Notice we're only writing the outer ring
        for vert in poly[0]:
            row = []
            row.extend(idAndFields)
            row.append(subPolygonId)
            row.append(pointId)
            row.append(vert.x())
            row.append(vert.y())
            # Convert the row to strings
            row = map(unicode, row)
            self.writer.writerow(row)
            pointId += 1
