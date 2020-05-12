[
    // element
    Footprint {
        // attributes with simple expression
        topHeight : 0.0;
        roofShape : "flat";

        // attributes with functions
        levelHeight : RandomNormal(3.);
        numLevels : RandomWeighted( ( (4, 10), (5, 40), (6, 10) ) );
        minHeight: Attr("min_height");

        // special case: OSM-attr that creates alternatives
        roofDirection: Attr("roof:direction");

        // alternatives
        roofShape : Attr("roof:shape") | "flat" | RandomWeighted(( ("gabled", 10), ("flat", 40) ));
    },
    Facade {
        defName : "brown_brick";
    }
]

