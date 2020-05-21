styles : {
    "mid rise residential zaandam": [
        meta {
            buildingUse : "residential";
            buildingLaf : "modern";
            height : "mid rise";
        },

        footprint {
            height : attr("height");
            minHeight : attr("min_height");
            numLevels : attr("building:levels") | random_weighted( ( (4, 10), (5, 40), (6, 10) ) );
            hasNumLevelsAttr : attr("building:levels");
            minLevel : attr("building:min_level") | 0.0;
            topHeight : 0.;
            levelHeight : random_normal(3.);
            groundLevelHeight : random_normal(4.2);
            bottomHeight : random_normal(1.);
            roofShape : attr("roof:shape") | "flat" | "saltbox" | random_weighted( ( ("gabled", 10), ("flat", 40) ) );
            roofHeight : attr("roof:height") | 5.0;
            roofAngle : attr("roof:angle");
            roofDirection : attr("roof:direction") | attr("roof:slope:direction");
            roofOrientation : "across";
            lastLevelOffsetFactor : random_weighted ((
                (0., 50), (0.05, 3), (0.1, 5), (0.15, 5), (0.2, 5), (0.25, 5), (0.3, 5),
                (0.35, 5), (0.4, 5), (0.45, 5), (0.5, 3), (0.55, 2), (0.6, 2)
            ));
            claddingColor : random_weighted ((  // PerBuilding not yet implemented
                ((0.647, 0.165, 0.165, 1.), 1), // brown
                ((0.565, 0.933, 0.565, 1.), 1), // lightgreen
                ((1., 0.855, 0.725, 1.), 1)     // peachpuff
            ));
            claddingMaterial : "brick";
        },

        facade@brown_brick {        
        },

        level@level_window_balcony {
            markup : [
                window {
                    width : 1.8;
                    height : 2.1;
                    rows : 1;
                    panels : 2;
                },
                balcony{}
            ]
        },

        level@staircase {
            // offset : (0.5, units.Level)  // data type not yet implemented
        },

        window@back_facade_window {
            width : 1.2;
            height : 1.8;
            panels : 1;
        },

        window@roof_window {
            width : 0.8;
            height : 0.8;
            rows : 1;
            panels : 1;

        },

        div@window_and_balcony {
            label : "Window and balcony";
            markup : [
                level {
                    // use = ("level_window_balcony",), // resulting data type not yet implemented
                    indices : (4, -1);
                    claddingMaterial : "plaster";
                    claddingColor : (0., 0., 1., 1.);  // blue
                },
                level {
                    // use = ("level_window_balcony",), // resulting data type not yet implemented
                    indices : (3, 3);
                    claddingColor : (0., 0.502, 0., 1.); // green
                },
                level{
                    // use = ("level_window_balcony",), // resulting data type not yet implemented
                    indices : (0, 2);
                },
                bottom {
                    markup : [
                        window{
                            width : 1.;
                            height : 1.;
                            rows : 1;
                            panels : 1;
                        }
                    ]
                }
            ]
        },

        div@staircase {
            label : "Staircase";
            bottomHeight : 0;
            markup : [
                level {
                    // repeat : False;  // Booleans not yet implemented PML: True or true ?
                    indices : (1, -1);
                    markup : [
                        window {
                            width : 0.8;
                            height : 0.8;
                            rows : 1;
                            panels : 1;
                        }
                    ]
                },
                level {
                    indices : (0, 0);
                    markup : [
                        door {
                            label : "entrance door";
                        }
                    ]
                }
            ]
        },

        div@roof_side {
            // width : use_from("main_section");    // function not yet implemented
            // symmetry : right-most-of-last;       // data type not yet implemented
        },

        facade[item.footprint.height - item.footprint.minHeight < minHeightForLevels] {
            label : "cladding only for too low structures";
        },

        facade[item.front] {
            // use: brown_brick;        // resulting data type not yet implemented
            label : "front facade";
            // symmetry = middle-of-last;       // data type not yet implemented
            // symmetryFlip : True              // Booleans not yet implemented PML: True or true ?
            markup : [
                div {
                    // use = ("window_and_balcony",), // resulting data type not yet implemented
                    id : "main_section";
                    label : "Window and Balcony";
                },
                div {
                    // use = ("staircase",),    // resulting data type not yet implemented
                    label : "Staircase";
                }
            ] 
        },

        facade[item.back] {
            // use: brown_brick;        // resulting data type not yet implemented
            label : "back facade";
            markup : [
                level{
                    indices : (0, -1);
                    markup : [
                        balcony{},
                        window{}, // use = ("back_facade_window",)),    // resulting data type not yet implemented
                        Window{}  // use = ("back_facade_window",))     // resulting data type not yet implemented
                    ]
                }
            ]
        },

        roof {
            claddingMaterial : "brick";
            claddingColor : (0.98, 0.502, 0.447, 1.); // salmon
            // faces : smoothness.Smooth;       // data type not yet implemented 
            // sharpEdges : smoothness.Side;    // data type not yet implemented
        },

        roofSide[item.front] {                  // camel case ?????  or roof-side ?
            markup : [
                div {
                    // use = ("roof_side",),    // data type not yet implemented
                    markup : [
                        // openable skylight or roof window
                        Window{}, //(use = ("roof_window",)),    // data type not yet implemented 
                        Window{}  //(use = ("roof_window",))     // data type not yet implemented 
                    ]
                }
            ]
        },

        roofSide[item.back] {                  // camel case ?????  or roof-side ?
            markup = [
                div {
                    // use = ("roof_side",),    // data type not yet implemented
                    markup : [
                        dormer{}, Dormer{}
                    ]
                }
            ]
        },

        ridge {
            markup : [
                div {
                    // width = useFrom("main_section"), // useFrom not yet implemented
                    // repeat : False,      // Booleans not yet implemented PML: True or true ?
                    markup : [
                        Chimney{}
                    ]
                }
            ]    
        }
    ]
}

