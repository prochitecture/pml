class Dictionaries():
    # only fragment, to be completed for all possible OSM-attributes
    def __init__(self):
        self.osm_attrs = {
            '"height"': [ "FromAttr.Float, FromAttr.Positive" ],
            '"min_height"': [ "FromAttr.Float, FromAttr.Positive" ],
            '"building:levels"': [ "FromAttr.Integer, FromAttr.Positive" ],
            '"building:min_level"': [ "FromAttr.Integer, FromAttr.NonNegative" ],
            '"building:material"': ["FromAttr.String, CladdingMaterials" ],
            '"building:colour"': [ "FromAttr.Color" ],
            '"roof:material"': ["FromAttr.String, CladdingMaterials"],
            '"roof:colour"': [ "FromAttr.Color" ],
            '"roof:shape"': [ "FromAttr.String, RoofShapes" ],
            '"roof:height"': [ "FromAttr.Float, FromAttr.NonNegative" ],
            '"roof:angle"': [ "FromAttr.Float" ],
            '"roof:direction"': [ "FromAttr.String, RoofDefs.directions", "FromAttr.Float" ],
            '"roof:slope:direction"': [ "FromAttr.String, RoofDefs.directions", "FromAttr.Float" ]
        }

    def getAttributeTypes(self,attribute):
        if attribute not in self.osm_attrs.keys():
            raise Exception('Dictionary ERROR: atrribute {} is not in dictionary'.format(attribute))
        else:
            return self.osm_attrs[attribute]
