@name "high rise";

@meta{
	buildingUse: office;
	buildingLaf: modern;
	height: "high rise";
}

footprint{
	height: attr("height");
	minHeight: attr("min_height");
	hasNumLevelsAttr: attr("building:levels");
	numLevels: attr("building:levels") | random_weighted( (4, 10), (5, 40), (6, 10) );
	minLevel: attr("building:min_level") | 0;
	topHeight: 0.;
	levelHeight: random_normal(3.);
	roofShape: attr("roof:shape") | flat;
	roofHeight: attr("roof:height");
	claddingMaterial: attr("building:material") | random_weighted( (brick, 1), (plaster, 1) );
	claddingColor: attr("building:colour")
		|
		if (item["claddingMaterial"] == "brick") random_weighted(
			((0.647, 0.165, 0.165, 1.), 1), // brown
			((0.98, 0.502, 0.447, 1.), 1), // salmon
			((0.502, 0., 0., 1.), 1) // maroon
		)
		;
}