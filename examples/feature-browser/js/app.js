//most of this stuff is straight out of trailhead.js

var app = {};
app.trails = [];
app.loops = [];
app.currentLoopPolyline = null;
app.map = null;
app.currentPositionMarker = null;
app.currentPositionIcon = null;
app.season = "summer"; //"summer" or "winter" or "mud"
app.activity = "foot"; //"foot" or "bike" or "ski"

app.centerOn = function(lat, lon, zoomLevel) {
	app.map.setView([lat,lon], zoomLevel)
};

app.setMode = function(season, activity) {
	app.season = season;
	app.activity = activity;
	app.drawTrails();
	app.setupOptions();
};

//this expects to be called from the shell whenever new trails need to be injected into the app
app.loadTrails = function(geojson) {
	//TODO: this would be a good place to do a MultiLineString vs LineString check
	for(var i = 0; i < geojson.features.length; i++) {
		app.trails.push(geojson.features[i]);
	}
};

app.loadLoops = function(geojson) {
	for(var i = 0; i < geojson.features.length; i++) {
		app.loops.push(geojson.features[i]);
	}
};

app.updateButton = function() {
	var buttons = document.getElementsByClassName("mode-button");
};

app.pins = [];

app.dropPin = function(lat, lon, tag) {
	var icon = L.icon({
    	iconUrl: 'icons/point.png',
    	iconRetinaUrl: 'icons/point@2x.png',
    	iconSize:[25,25]
    });

	var pin = L.marker([lat, lon], {
		icon: icon
	});
	pin.tag = tag;
	pin.on('click', app.pinClicked);
	app.pins.push(pin);
	pin.addTo(app.map);
};

app.clearPins = function() {
	for(var i = 0; i < app.pins.length; i++)
		app.map.removeLayer(app.pins[i]);
	app.pins = [];
};

app.pinClicked = function(e)
{
	var pin = e.target;
	var loc = pin.getLatLng();
	var tag = pin.tag;
	location.assign("action:pinclicked?lat=" + loc.lat + "&lon=" + loc.lng + "&tag=" + tag);
};

app.setSeason = function(s) {
	app.season = s;
	if(app.activity == "ski" && app.season != "winter")
		app.activity = "foot";
	app.drawTrails();
	app.setupOptions();
};

app.setActivity = function(a) {
	app.activity = a;
	if(app.activity == "ski" && app.season != "winter")
		app.activity = "foot";
	app.drawTrails();
	app.setupOptions();
};

app.setBounds = function(swLat, swLon, neLat, neLon) {
	var bounds = L.latLngBounds(L.latLng(swLat, swLon), L.latLng(neLat, neLon));
	app.map.setMaxBounds(bounds);
};

app.showOptions = function() {
	document.getElementById("map-options").style.display = "block";
};

app.hideOptions = function() {
	document.getElementById("map-options").style.display = "none";
};

app.toggleOptions = function() {
	if(document.getElementById("map-options").style.display != "block")
		 app.showOptions();
	else
		app.hideOptions();
};

app.showCurrentPosition = function(lat,lon,heading) {
	if(app.currentPositionMarker == null)
	{
		app.currentPositionIcon = L.icon({
		    iconUrl: 'icons/currentlocation.png',
		    iconRetinaUrl: 'icons/currentlocation@2x.png',
		    iconSize: [33,33]
		});

		var opts = {icon:app.currentPositionIcon};
		if(heading)
			opts.angle = heading;

		app.currentPositionMarker = L.rotatedMarker([lat,lon], opts).addTo(app.map);
	}
	else
	{
		if(heading)
			app.currentPositionMarker.options.angle = heading;
		app.currentPositionMarker.setLatLng(L.latLng(lat,lon));
		app.currentPositionMarker.setOpacity(1);
	}
};

app.hideCurrentPosition = function() {
	if(app.currentPositionMarker != null)
		app.currentPositionMarker.setOpacity(0);
};

app.highlightTrail = function(name, openPopup) {
	var popupWasOpened = false;
	for (var i = 0; i < app.trails.length; i++) 
    {
    	var currseg = app.trails[i];
    	if(currseg.mapBackgroundLine)
    	{
    		if(!name) //if name is not passed in, all highlighting is turned off
    			currseg.mapBackgroundLine.setStyle({opacity:0});
	    	else if(!app.segmentIsInScope(currseg)) //if segment is out of scope, don't highlight
	    		currseg.mapBackgroundLine.setStyle({opacity:0});
	    	else if(currseg.properties.Name == name && currseg.properties.Name != "Unnamed") //if names match, highlight (except Unnamed)
			{
	    		currseg.mapBackgroundLine.setStyle({opacity:0.5});
	    		if(openPopup && openPopup == true && popupWasOpened == false)
	    		{
	    			currseg.mapBackgroundLine.openPopup();
	    			popupWasOpened = true;
	    		}
	    	}
	    	else
				currseg.mapBackgroundLine.setStyle({opacity:0});
		}
    }
};

app.trailClicked = function(e) {
	//to dig stuff out of the segment, use e.target.segment.properties.trail_name
	//alert(e.target.segment.properties.trail_name);
	var segment = e.target.segment;
	app.highlightTrail(segment.properties.Name);
};

app.initialize = function(htmlElementID, callback) {

    app.map = L.map(htmlElementID);
    app.map.attributionControl = null; //make it go away

    //this is a requirement - got to tell leaflet where to get tiles
    //tiles directory is in the front-end app's project directory
    L.tileLayer('tiles/{z}/{x}/{y}.jpg', {
      maxZoom: 18,
      minZoom:13,
      attribution: ''
    }).addTo(app.map);

    app.drawTrails();
    app.setupOptions();

    if(callback)
		callback();
};

app.segmentIsInScope = function(segment) {
	if((app.season == "summer" || app.season == "mud") && app.activity == "bike" && (segment.properties.System == "Kincaid Single Track" || segment.properties.System == "Kincaid Ski Trails" || segment.properties.System == "Coastal Trail"))
   		return true;
   else if(app.season == "winter" && app.activity == "bike" && segment.properties.System == "Kincaid Single Track")
   		return true;
	else if(app.season == "winter" && app.activity == "ski" && (segment.properties.System == "Kincaid Ski Trails" || segment.properties.System == "Coastal Trail"))
   		return true;
	else if((app.season == "summer" || app.season == "mud") && app.activity == "foot" && (segment.properties.System == "Kincaid Ski Trails" || segment.properties.System == "Coastal Trail" || segment.properties.System == "Kincaid Other Trails"))
   		return true;
	else if((app.season == "winter") && app.activity == "foot" && (segment.properties.System == "Coastal Trail"))
   		return true;
   	else
   		return false;
};

app.setupOptions = function() {
	//setup mode buttons
	var buttons = document.getElementsByClassName("mode-button");
	for(var i = 0; i < buttons.length; i++)
		buttons[i].style.backgroundColor = "white";

	document.getElementById(app.season + "-season").style.backgroundColor = "yellow";
	document.getElementById(app.activity + "-activity").style.backgroundColor = "yellow";

   	var trails = app.trailsByName();
	var html = "";
	for(var k in trails)
	{
		if(k && k != "Unnamed" && k != null)
			html += "<div class='trail-name' onclick=\"app.selectTrail('" + k.replace("'", "\\'") + "');\">" + k + "</div>";
	}
	document.getElementById("known-trails").innerHTML = html;

	var loopHtml = "";
	if(app.loops != null)
	{
		for(var i = 0; i < app.loops.length; i++)
		{
			loopHtml += "<div class='loop-name' onclick=\"app.selectLoop(" + i + ");\">" + app.loops[i].properties.Name + "</div>";
		}
	}
	document.getElementById("known-loops").innerHTML = loopHtml;


};

app.selectTrail = function(name) {
	app.highlightTrail(name, true);
	app.hideOptions();
};

app.selectLoop = function(index) {
	var loop = app.loops[index];
	app.showLoop(loop);
	app.hideOptions();
};

app.showLoop = function(loop) {
	var points = [];
	for (var j = 0; j < loop.geometry.coordinates.length; j++) 
   	{
    	points[points.length] = L.latLng(loop.geometry.coordinates[j][1], loop.geometry.coordinates[j][0]);
	}

	if(app.currentLoopPolyline == null)
	{
		app.currentLoopPolyline = L.polyline(points, {color:"orange", opacity:0.7, weight:10}).addTo(app.map);
	}
	else
	{
		app.currentLoopPolyline.setLatLngs(points);
		app.currentLoopPolyline.redraw();
	}
};

app.trailsByName = function() {
   	var dict = {};

   	for (var i = 0; i < app.trails.length; i++) 
    {
       var segment = app.trails[i];

       if(app.segmentIsInScope(segment))
       {
       		var name = segment.properties.Name;
       		if(name in dict)
       			dict[name].push(segment);
       		else 
				dict[name] = [segment];       			
       }
    }
	return dict;
};

app.drawTrails = function() {
	//add trail polylines
	app.clearMap();
    var foreLines = [];
    if(app.trails != null && app.trails)
    {
	    for (var i = 0; i < app.trails.length; i++) 
	    {
	       var segment = app.trails[i];

	       if(app.segmentIsInScope(segment))
	       {
		       var points = [];
		       for (var j = 0; j < segment.geometry.coordinates.length; j++) 
		       		points[points.length] = L.latLng(segment.geometry.coordinates[j][1], segment.geometry.coordinates[j][0]);

	          //major trails are width 3
	          //single track are width 2
	          //minor trails are width 1

	          var lineOptions = {color:"brown", opacity:1, weight:3};
	          var bgLineOptions = {color:"yellow", opacity:0, weight:20};

	          if(segment.properties.System == "Kincaid Ski Trails")
	          {
	          	lineOptions.weight = 3;
	          	lineOptions.color = "green";
	          }
	         else if(segment.properties.System == "Kincaid Single Track")
			 {
				lineOptions.weight = 2;
	          	lineOptions.color = "brown";
	         }
			 else if(segment.properties.System == "Kincaid Other Trails")
			 {
				lineOptions.weight = 1;
	          	lineOptions.color = "gray";
	          	lineOptions.dashArray = "1,1";
	         }
			 else if(segment.properties.System == "Coastal Trail")
			 {
				lineOptions.weight = 3;
	          	lineOptions.color = "gray";
	         }

	          if(segment.properties.Difficulty && app.activity == "ski")
	          {
	            if(segment.properties.Difficulty.toLowerCase() == 'novice')
	              lineOptions.color = 'green';
	            else if(segment.properties.Difficulty.toLowerCase() == 'intermediate')
	              lineOptions.color = 'blue';
	            else if(segment.properties.Difficulty.toLowerCase() == 'advanced')
	              lineOptions.color = 'black';
	          }

	          if(segment.properties.SkiType && segment.properties.SkiType == "classic" && app.activity == "ski")
	            lineOptions.dashArray = "5,5";

	          //the background polyline
	          var polyline = L.polyline(points, bgLineOptions).addTo(app.map);
	          polyline.bindPopup(app.popupHtml(segment));
	          polyline.segment = segment;
	          polyline.on('click', app.trailClicked);
	          segment.mapBackgroundLine = polyline; //remember it so that we can manipulate it later

	          //foreground
	          var foreLine = L.polyline(points, lineOptions); //.addTo(app.map);
	          foreLine.bindPopup(app.popupHtml(segment));
	          foreLine.segment = segment;
	          foreLine.on('click', app.trailClicked);
	          segment.mapForegroundLine = foreLine; //remember it so that we can manipulate it later
	          foreLines[foreLines.length] = foreLine; //defer adding so that line joints don't overlap in an ugly way
		   	}
		}
	  }

    //little hack to get the foreground paths to be added after ALL background segments
   	for(var i = 0; i < foreLines.length;i++)
   		foreLines[i].addTo(app.map);

};

app.clearMap = function() {
    for(i in app.map._layers) {
        if(app.map._layers[i]._path != undefined) {
            app.map.removeLayer(app.map._layers[i]);
        }
    }
}

app.popupHtml = function(segment){
	var h = "";
	if(segment.properties.Name)
		h += "<h3>" + segment.properties.Name + "</h3>";

	if(app.activity == "ski")
	{
		if(segment.properties.Difficult)
			h += "<div>" + segment.properties.Difficult + "</div>";
		if(segment.properties.SkiType && segment.properties.SkiType == "classic")
			h += "<div>Classic Only</div>";
	}

	return h;
};