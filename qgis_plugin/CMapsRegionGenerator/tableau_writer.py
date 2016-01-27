from qgis.core import QGis
import csv



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
        self.nextFeatureId = 1
        try:
            self.file = open(self.fileName, 'wb')
        except IOError:
            raise TableauFileCreationError()
        self.writer = csv.writer(self.file)
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
        TODO:  How do features with holes get treated in terms of their SubPolygonId column?
        At present we assume there are no holes
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
        elif feature.geometry().wkbType() == QGis.WKBMultiPolygon:
            polys = feature.geometry().asMultiPolygon()
            partNo = 1
            for poly in polys:
                self._writePolygon(idAndFields, partNo, poly)
                partNo += 1
        else:
            raise TableauUnexpectedGeometryTypeError()

    def _writePolygon(self, idAndFields, subPolygonId, poly):
        if len(poly) < 1:
            raise TableauGeometryError('Polygon had 0 rings')
        elif len(poly) > 1:
            # FIXME
            # raise TableauGeometryError('Polygon had more than 1 ring')
            pass
        pointId = 1
        for vert in poly[0]:
            row = []
            row.extend(idAndFields)
            row.append(subPolygonId)
            row.append(pointId)
            row.append(vert.x())
            row.append(vert.y())
            self.writer.writerow(row)
            pointId += 1
