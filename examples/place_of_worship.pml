//===================================================
//  PML file for Blender-OSM
//  Styles for "Place of worship" tag buildings
//===================================================
@name "place of worship";

footprint {
	height: attr("height");
	minHeight: attr("min_height");
	numLevels: 0;
	topHeight: 0.;
	roofShape: attr("roof:shape") | flat;
	roofHeight: attr("roof:height");
        buildingPart: attr("building:part");
	claddingMaterial: per_building(
		attr("building:material") | plaster
	);

}

//Cube -- main volume
facade 
[item.footprint["buildingPart"] == "cube"]
{
	claddingColor: (1., 0., 0., 1.);
	markup: [
		level{}
	]
}

//refectory
facade 
[item.footprint["buildingPart"] == "refectory"]
{
	claddingColor: (0., 1., 0., 1.);
}

// porch
facade 
[item.footprint["buildingPart"] == "porch"]
{
	claddingColor: (0., 0., 1., 1.);
}

// belltower
facade 
[item.footprint["buildingPart"] == "belltower"]
{
	claddingColor: (0., 0., 1., 1.);
}

//apse
facade 
[item.footprint["buildingPart"] == "apse"]
{
	claddingColor: (0., 0., 1., 1.);
}

facade 
[item.footprint["buildingPart"] == "tholobate"]
{
	claddingColor: (0., 0., 1., 1.);
}

//Unknown facade
facade 
{
//absolutely nothing
}


roof {
	roofCladdingMaterial: attr("roof:material") | metal;
	roofCladdingColor:
		attr("roof:colour")
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


