
/* functions of the map that don't need django template tags */


  /* location request. E.g. via GPS or wifi */
  function getLocation() {
    if (navigator.geolocation) {
      function error(){alert("No location available.")
      }
      const options = {enableHighAccuracy: true, // this may require additional premissions by the device
      }
      navigator.geolocation.getCurrentPosition(showPosition, error, options)
    }
    else {alert("Geolocation is not supported by this browser.")}
  }

  /* Zoom to the requested location and set a marker. */
  function showPosition(position) {
    /* Round coordinates to the 6th decimal. */
    var lat = String(Math.round(position.coords.latitude*1000000)/1000000)
    var lng = String(Math.round(position.coords.longitude*1000000)/1000000)
    // If a marker was already set reposition it
    if (activeMarker == true) {marker.setLatLng([lat,lng])}
    // If no marker is active, create a new marker
    else {
      marker = new L.marker([lat,lng],
        {
          draggable:'true',
          icon: pinIcon,
          zIndexOffset: 1000 // Place the pin above other layers.
        }
      ).addTo(map)
      marker.on("dragend", onDrag)
      activeMarker = true;
    }
    map.setView([lat, lng], 16) // Set the zoom level
  }

  /* to diferentiate a hover info panel from a clicked one.
   This is needed so the info panel stays open for flaging pictures.*/
  function clickOpen(e){

    if (clickedElement != null){
      console.log(clickedElement.className)
      if (clickedElement.className != "simple2category4" & clickedElement.className != "simple2category3"){
        clickedElement.style.borderStyle = "none"
        clicked = false
      }

    }

    // if Icon without concentric rings
    clickedElement = e.target._icon.children[1]
    // if Icon with concentric rings for own observations
    if (e.target._icon.children.length > 2) {
      clickedElement = e.target._icon.children[4]
    }
      //clickedElement.style.borderWidth = "medium"
      if (clickedElement.className != "simple2category4" & clickedElement.className != "simple2category3"){
        clickedElement.style.borderStyle = "solid"
      } else {
        // borderColorRiskMap = clickedElement.style.borderBottomColor
        clickedElement.style.borderBottomColor = "#134a74"
      }

    clicked = false
    resetHighlight(e)
    highlightFeature(e)
    // pan to clicked marker

    //disable panning, scrolling and zooming to prevent cluster markers
    // to throww errors when opening a marker via click
    map.dragging.disable();
    map.touchZoom.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();


    clicked = true
    // limit full info to these observation types
    if (e.target.options.observation == "category1" || e.target.options.observation == "category2" || e.target.options.observation == "category3" || e.target.options.observation == "category4"){
      var k = e.target.options.creationDate.toString().concat(e.target.options.observation, e.target.options.oid)
      // Manage the information table shown in the sidebar
      show_content_fullinfo(fullinfodict[k])
    }
  }

  /* Function for building a custom leaflet control button that allows for location requests. */
  var locationButton = L.Control.extend(
    {
    options:
      {
        position: 'bottomright'
      },
      onAdd: function (map) {
        /* Create a DOM-Util with the default style of a leaflet button
        and customize it a little. */
        var container = L.DomUtil.create(
          'div',
          'leaflet-bar leaflet-control leaflet-control-position'
          )
        L.DomEvent.disableClickPropagation(container)
        container.style.backgroundColor = 'white'
        container.style.width = '30px'
        container.style.height = '30px'
        container.onclick = function(){getLocation()}
        // disable pins  or panning under button
        L.DomEvent.on(container, "click", L.DomEvent.stopPropagation)
        return container
      },
    })


function splitCluster(){
  layercontrol.remove()
  clustercontainer.remove()
  //remove layer control group with clustered groups and add declustered groups)
  if (clusteredicons == true){
    if (map.hasLayer(category1LayerGroup)){
      category1points.addTo(map)
    }
    category1LayerGroup.remove()
    if (map.hasLayer(category4LayerGroup)){
      category4points.addTo(map)
    }
    category4LayerGroup.remove()
    if (map.hasLayer(category2LayerGroup)){
      category2points.addTo(map)
    }
    category2LayerGroup.remove()
    if (map.hasLayer(category3LayerGroup)){
      category3points.addTo(map)
    }
    category3LayerGroup.remove()
    optionalLayerKeys = {
      "category1": category1points,
      "category2": category2points,
      "category3": category3points,
      "category4": category4points,
    }
    clusterbuttonimg = 'merge_cluster'
    clusteredicons = false
  } else {
    if (map.hasLayer(category1points)){
      category1LayerGroup.addTo(map)
    }
    category1points.remove()
    if (map.hasLayer(category4points)){
      category4LayerGroup.addTo(map)
    }
    category4points.remove()
    if (map.hasLayer(category2points)){
      category2LayerGroup.addTo(map)
    }
    category2points.remove()
    if (map.hasLayer(category3points)){
      category3LayerGroup.addTo(map)
    }
    category3points.remove()

    optionalLayerKeys = {
      "category1": category1LayerGroup,
      "category2": category2LayerGroup,
      "category3": category3LayerGroup,
      "category4": category4LayerGroup,
    }
    clusterbuttonimg = 'split_cluster'
    clusteredicons = true
  }
  layercontrol = L.control.layers(basemaps,optionalLayerKeys)
  layercontrol.addTo(map)
  map.addControl(new splitClusterButton())
}

  var splitClusterButton = L.Control.extend(
    {
    options:
      {position: 'topright'},
      onAdd: function (map) {
        clustercontainer = L.DomUtil.create(
          'div',
          'leaflet-bar leaflet-control splitcluster'
          )
        L.DomEvent.disableClickPropagation(clustercontainer)
        clustercontainer.style.backgroundColor = 'white'
        clustercontainer.style.padding = "5px 5px 5px 7px"
        clustercontainer.innerHTML = "<img src='"+ static_path + "image/" + clusterbuttonimg + ".svg' style='max-width: 100%; max-height: 100%;'/>"
        clustercontainer.style.width = '46px'
        clustercontainer.style.height = '46px'
        clustercontainer.onclick = function(){splitCluster()}
        L.DomEvent.on(clustercontainer, "click", L.DomEvent.stopPropagation)
        return clustercontainer
      },
    })

/* Building the custom cluster group icons. */
function returnClusterIcon(iconType, ringe){
  if (ringe == true){
    /* Building the inner HTML. */
    var html =  "<div class='" + iconType + "Ring1'></div><div class='" +
                iconType + "Ring2'></div><div class='" + iconType +
                "Ring3'></div>" + "<img class = '" + iconType +
                "Icon' src='"+static_path+"image/" + iconType + ".svg'/>" +
                "<div class='clusterField'>"
  } else {
    var html =  "<img class='clusterIcon' src='"+static_path+ "image/" +
                iconType + ".svg'/>" + "<div class='clusterField'>"
  }
  /* Building MarkerCluster. */
  var customClusterIcon = L.markerClusterGroup(
    {
      iconCreateFunction: function (cluster) {
        var markers = cluster.getAllChildMarkers()
        var n = 0;
        // Manage the number of clustered icons
        for (var i = 0; i < markers.length; i++) {
          n = markers.length
        }

        var clustericon = L.divIcon(
          {
           html: html + n + "</div>",
           className: 'clusterBox',
           iconSize: L.point(24, 24)
         })
        return   clustericon
      },
      polygonOptions: {color: '#134a74'},
    })
  return customClusterIcon
}

/* On highlighting a marker fetch information and build the html for
an info panel. */
function highlightFeature(e) {
    infoOpen = true
    var t = e.target.options.observation
    var l = e.target.options.label
    var i = e.target.options.primaryInfo
    var i2 = e.target.options.secondaryInfo
    var i3 = e.target.options.tertiaryInfo
    var i4 = e.target.options.quaternaryInfo
    var i5 = e.target.options.quinaryInfo
    var od = e.target.options.observationDate
    var p = e.target.options.photo
    var uid = e.target.options.uid
    var iDescription = ""
    var i2Description = ""
    if (i2 == "" | i2 == null) {
        i2 = "NaN"
    }
    if (i3 == "" | i3 == null) {
        i3 = "NaN"
    }
    if (i4 == "" | i4 == null) {
        i4 = "NaN"
    }
    if (i5 == "" | i5 == null) {
        i5 = "NaN"
    }

    if (t == "category1") {
        description1 = "attribute 1: "
        description2 = "attribute 2: "
        description3 = "attribute 3:"
        i3 = ""
    } else if (t == "category2") {
        description1 = "attribute 1: "
        description2 = "attribute 2: "
        description3 = "attribute 3: "
        i3 = ""
    } else if (t == "category3") {
      description1 = "attribute 1: "
      description2 = "attribute 2: "
      description3 = "attribute 3: "
        i2 = e.target.options.quaternaryInfo
        i3 = e.target.options.quinaryInfo
        i3 = ""
    } else if (t == "category4") {
      description1 = "attribute 1: "
      description2 = "attribute 2: "
      description3 = "attribute 3: "
        i = e.target.options.secondaryInfo
        i2 = e.target.options.tertiaryInfo
        i3 = ""
    }

    /* Check if there should be drawn a photo. */
    var infoImg = ""
    if (p != "no photo") {
      // Construct an image DOM with the photo url.
        infoImg = "<img src='" + p + "' class = \"infoImage\"/>"
      }

    var editlink = ""
    var typelink = ""
    var deletelink = ""
      if(e.target.options.observation == "category4"){
        typelink = "category4"
      }
      if(e.target.options.observation == "category2"){
        typelink = "category2"
      }
      if(e.target.options.observation == "category3"){
        typelink = "category3"
      }
      if(e.target.options.observation == "category1"){
        typelink = "category1"
      }
    // if this is one of your own entries allow editing
    if (active_user == e.target.options.uid){
      editlink = "    <a href='/observations/update"+typelink+"/"+e.target.options.oid+"/'><img alt='update entry' src='"+static_path+"image/edit_icon.svg' height = '16px'/></a>"
      deletelink = "    <a href='/observations/delete"+typelink+"/"+e.target.options.oid+"/'><img alt='delete entry' src='"+static_path+"image/icon_delete.svg' height = '16px'/></a>"
    }

    // example values that can be displayed on info
    var displayed_name = "anonym"
    if (userdict[uid] != undefined){
      displayed_name = userdict[uid]
    }



    var comment = ""
    if (e.target.options.report == 1){
      comment = '<i style="color: red;"> Photo was reported.</i><br/>'
    }
    if (e.target.options.report == 2){
      comment = '<i style="color: red;"> Values were reported as wrong.</i><br/>'
    }
    if (e.target.options.report == 3){
      comment = '<i style="color: red;"> Reported for other reasons.</i><br/>'
    }
    if (e.target.options.report == 4){
      comment = '<i style="color: red;"> High GPS-inaccuracy.</i><br/>'
    }


    /* String to uild innerHTML of the info panel*/
    var htmlHighlight = "<div id=\"infobox-contain\"><div id=\"head\"><b>" + l + editlink + deletelink +
      "</b><button style=\"float: right; border: 0; box-shadow: none; background: none;\" value= "+typelink+","+e.target.options.oid+">" +
         "<img class ='flagIcon' src='"+static_path+"image/warning.svg' height = '20px'/>" +
       "</button></div>" +
      // use this if we get the ok for showing user names
      //"<b> Erfasst: "+ userlist[uid-1] +"<br/>" + od +  "<br/>" +
      "<b> Recorded by: "+ displayed_name + "<br/>" + od +  "<br/>" + comment +
      description1 + i + "<br/>" +
      description2 + i2 + "<br/>" +
      description3 + i3 + "<br/><b style=\"cursor: pointer\" onclick=open_fullinfo() >more information</b> <br/>"+
      infoImg + "</b></div>"


    info._div.style.display = "flex"
    info._div.style.maxWidth = "40vw"
    info._div.style.maxHeight = "60vh"
    // Test if screen has mobile size
    mqList = window.matchMedia("(max-width:767px)")
    if (mqList.matches == true){
        //info._div.style.overflowY = "auto"
        info._div.style.maxWidth = "80vw"
    }
    info.update(htmlHighlight,e)
}

/* Clear the info panel. */
function resetHighlight(e) {
  // close when not clicked info panel
  if (clicked == false){ //??? problem hier???
    infoOpen = false
    var layer = e.target;
    info._div.style.display = "none"
    info.update("<b id=\"head\">Info.</b>", e);
    map.dragging.enable();
    map.touchZoom.enable();
    map.doubleClickZoom.enable();
    map.scrollWheelZoom.enable();
  }
}

/* Build the the custom observation icons. */
function returnIcon(iconType, cat, ringe){

  if (iconType.includes("simple")){
    if (iconType.includes("simple1")){
      var html = "<div class='" + iconType.replace("simple1","") + "Wave'></div>" +
                      "<div class = '" + iconType.replace("1","")  + "' " + "></div>"
    }
    else if (iconType.includes("simple2")){
      var html = "<div class='" + iconType.replace("simple2","") + "Wave'></div>" +
                      "<div class = '" + iconType  + "' " + "></div>"
    } else {
      var html = "<div class='" + iconType.replace("simple","") + "Wave'></div>" +
                      "<div class = '" + iconType + "'></div>"
    }
  } else{
    /* Separate the design with concentrical rings for own observations in Markercluster mode. */
    if (ringe == true){
      var html =  "<div class='" + iconType + "Wave'></div>" +
                  "<div class='" + iconType + "Ring1'></div><div class='" +
                  iconType + "Ring2'></div><div class='" + iconType +
                  "Ring3'></div>" + "<img class = '" + iconType +
                  "Icon' src='"+ static_path + "image/" + iconType + ".svg'/>"
    } else {
      var html = "<div class='" + iconType + "Wave'></div>" +
                      "<img class = '" + iconType +
                      "Icon' src='"+ static_path + "image/" + iconType + ".svg'/>"
    }
  }
  var customIcon = L.divIcon({html: html,
                  className: 'circlebox', iconSize: (20,20)})
  return customIcon
}

/* Building the custom cluster group icons. */
function returnClusterIcon(iconType, ringe){
  if (ringe == true){
    /* Building the inner HTML. */
    var html =  "<div class='" + iconType + "Ring1'></div><div class='" +
                iconType + "Ring2'></div><div class='" + iconType +
                "Ring3'></div>" + "<img class = '" + iconType +
                "Icon' src='"+static_path+"image/" + iconType + ".svg'/>" +
                "<div class='clusterField'>"
  } else {
    var html =  "<img class='clusterIcon' src='"+static_path+ "image/" +
                iconType + ".svg'/>" + "<div class='clusterField'>"
  }
  /* Building MarkerCluster. */
  var customClusterIcon = L.markerClusterGroup(
    {
      iconCreateFunction: function (cluster) {
        var markers = cluster.getAllChildMarkers()
        var n = 0;
        // Manage the number of clustered icons
        for (var i = 0; i < markers.length; i++) {
          n = markers.length
        }

        var clustericon = L.divIcon(
          {
           html: html + n + "</div>",
           className: 'clusterBox',
           iconSize: L.point(24, 24)
         })
        return   clustericon
      },
      polygonOptions: {color: '#134a74'},
    })
  return customClusterIcon
}


  // shorten German month names to numeric
  function shorten_date(str){
    var monthdict = {" Januar ":"01."," Februar ":"02."," März ":"03.",
    " April ":"04.", " Mai ":"05."," Juni ":"06."," Juli ":"07."," August ":"08.",
    " September ":"09."," Oktober ":"10."," November ":"11."," Dezember ":"12."}

    for (m in monthdict) {
      if (str.includes(m)){str = str.replace(m, monthdict[m])
        break
      }
    }
    // add leading zeroes to the day <
    if (str.split(".")[0].length < 2){
      str = "0" + str
    }
    return str
  }

  // to sort new entries by observation date not entry date
  function sortable_date(str){
    str = str.split(".")
    str = str.reverse()
    str = str.join("")
    return parseInt(str)

  }


function lableFeatures(feature, layer){
  layer.bindPopup(feature.properties.NAME)
}


// zooms to entry from recent activity list
function zoomTo(lat,lng){
  map.setView([lat, lng], 17)
}

/* Add a dragable marker on left-click. */
function createMarker(e) {
  marker = new L.marker(e.latlng,
    {
      draggable:'true',
      icon: pinIcon,
      zIndexOffset: 1000
    })
  activeMarker = true
  /* Round them to the 6th decimal. */
  var lat = String(Math.round(e.latlng.lat*1000000)/1000000)
  var lng = String(Math.round(e.latlng.lng*1000000)/1000000)
  marker.addTo(map)
  // Bind a drag-function to the marker
  marker.on("dragend", onDrag);
  marker.bindPopup("Lat: " + lat + "<br/>" + "Lon: " + lng)
}


/* Change the popup and values in the input field on drag. You can also
add a function that fills an entry form with map coordinates here.*/
function onDrag(e){
  /* Round them to the 6th decimal. */
  var lat = String(Math.round(e.target.getLatLng().lat*1000000)/1000000)
  var lng = String(Math.round(e.target.getLatLng().lng*1000000)/1000000)
  var newPopupText =  "Lat: " + lat + "<br/>" + "Lon: " + lng
  this.bindPopup(newPopupText).openPopup()
}

/* Controls the active marker. */
function toggleMarker(e){
  try{
  /* don't change marker state if info panel is open. */
  if (infoOpen == false){
    if (activeMarker == false){
      createMarker(e)
      activeMarker = true
    } else {
      /* Remove the marker. */
      marker.remove()
      activeMarker = false

    }
  }
  clicked = false
  if (clickedElement != null){

    if (clickedElement.className.includes("simple2")){
    } else {
      clickedElement.style.borderStyle = "none"
    }
    remove_category3_poly()
  }

    // because not every time a marker object is selected
    resetHighlight(e)
  } catch {
    console.log("no marker clicked")
    if (clicked == false){
      infoOpen = false
      info._div.style.display = "none"
      map.dragging.enable();
      map.touchZoom.enable();
      map.doubleClickZoom.enable();
      map.scrollWheelZoom.enable();
    }
  }
}
