@name "high rise";

@meta {
	buildingUse: office;
	buildingLaf: modern;
	height: "high rise";
}

footprint {
	height: attr("height");
	minHeight: attr("min_height");
	hasNumLevelsAttr: attr("building:levels");
	numLevels: attr("building:levels") | random_weighted( (4, 10), (5, 40), (6, 10) );
	minLevel: attr("building:min_level") | 0;
	topHeight: 0.;
	levelHeight: random_normal(3.);
	roofShape: attr("roof:shape") | flat;
	roofHeight: attr("roof:height");
	claddingMaterial: per_building(
		attr("building:material") | random_weighted( (brick, 1), (plaster, 1) )
	);
	claddingColor: per_building(
		attr("building:colour")
		|
		if (item["claddingMaterial"] == "brick") random_weighted(
			((0.647, 0.165, 0.165, 1.), 1), // brown
			((0.98, 0.502, 0.447, 1.), 1), // salmon
			((0.502, 0., 0., 1.), 1) // maroon
		)
		|
		if (item["claddingMaterial"] == "plaster") random_weighted(
            ((1., 0.627, 0.478, 1.), 1), // lightsalmon
            ((0.565, 0.933, 0.565, 1.), 1), // lightgreen
            ((1., 0.855, 0.725, 1.), 1) // peachpuff
		)
		|
		if (item["claddingMaterial"] == "glass") random_weighted(
            ((0.306, 0.447, 0.573, 1.), 1),
            ((0.169, 0.318, 0.361, 1.), 1),
            ((0.094, 0.18, 0.271, 1.), 1)
		)
	);
}

facade[
	not item.footprint.numLevels or
	item.footprint.height - item.footprint.minHeight < 1.5 or // minHeightForLevels
	item.width < 1. // minWidthForOpenings
] {
	label: "cladding only for structures without levels or too low structures or too narrow facades";
}

facade[item.footprint["claddingMaterial"] == "glass"] {
	markup: [
		curtain_wall{}
	]
}

facade {
	markup: [
		level{}
	]
}

roof {
	roofCladdingMaterial:
		attr("roof:material")
		|
		if (item.footprint["roofShape"] == "flat") concrete
		|
		metal
	;
	roofCladdingColor:
		attr("roof:colour")
		|
		if (item["roofCladdingMaterial"] == "concrete") random_weighted(
            ((0.686, 0.686, 0.686, 1.), 1),
            ((0.698, 0.698, 0.651, 1.), 1),
            ((0.784, 0.761, 0.714, 1.), 1)
		)
		|
		// roofCladdingMaterial == "metal"
		random_weighted(
            ((0.686, 0.686, 0.686, 1.), 1),
            ((0.698, 0.698, 0.651, 1.), 1),
            ((0.784, 0.761, 0.714, 1.), 1)
		)
	;
	faces: if (item.footprint["roofShape"] in ("dome", "onion")) smooth;
}



@name "residential";

@meta {
	buildingUse: appartments;
	buildingLaf: modern;
	height: "high rise";
}