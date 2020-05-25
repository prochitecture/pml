@name "high rise";

meta{
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
	claddingColor: attr("building:colour") | if (item["claddingMaterial"] == "brick") white;
}