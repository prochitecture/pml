[
    Footprint(
        topHeight = 0.0,
        roofShape = "flat",
        levelHeight = Value(RandomNormal( 3. ),
        numLevels = Value(RandomWeighted( ((4,10),(5,40),(6,10)) ),
        minHeight = Value(FromAttr("min_height", FromAttr.Float, FromAttr.Positive),
        roofDirection = Value(Alternatives(
            FromAttr("roof:direction", FromAttr.String, RoofDefs.directions),
            FromAttr("roof:direction", FromAttr.Float)
        )),
        roofShape = Value(Alternatives(
            FromAttr("roof:shape", FromAttr.String, RoofShapes),
            Constant("flat"),
            RandomWeighted( (("gabled",10),("flat",40)) )
        ))
    ),
    Facade(
        defName = "brown_brick"
    )
]
