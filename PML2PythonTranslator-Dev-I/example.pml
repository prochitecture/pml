[
    // element
    footprint {
        // attributes with simple expression
        topHeight : 0.0;
        roofShape : flat;
        symmetry: rightmost-of-last;

        // attributes with functions
        levelHeight : random_normal(3.);
        numLevels : random_weighted( ( (4, 10), (5, 40), (6, 10) ) );
        minHeight: attr("min_height");

        // special case: OSM-attr that creates alternatives
        roofDirection: attr("roof:direction");

        // alternatives
        roofShape : attr("roof:shape") | flat | random_weighted(( (gabled, 10), ("flat", 40) ));
    },
    facade {
        label : "front facade";
    }
]

