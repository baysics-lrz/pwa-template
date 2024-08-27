/* Create a Leaflet map at a certrain view and zoom level. */
var map = L.map('map',{
  // Remove automatic zoom control so we can reposition it freely
  zoomControl:false
}).setView([49, 11], 7)

// Bright map with few labels (Carto Voyage style).
var CartoDB_VoyagerNoLabels = L.tileLayer(
  'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',
  {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  }).addTo(map)

/* Add the borders of the interaction area (i.e. Bavarian state border).*/
var bayerischeGrenze = L.geoJSON(
  bygrenze,
  {
    fill: null,
    color: "#134a74",
    weight: 1
  }).addTo(map)

map.fitBounds(bayerischeGrenze.getBounds())


var category1_color = getComputedStyle(document.documentElement).getPropertyValue('--category1-color')
var category2_color = getComputedStyle(document.documentElement).getPropertyValue('--category2-color')
var category3_color = getComputedStyle(document.documentElement).getPropertyValue('--category3-color')
var category4_color = getComputedStyle(document.documentElement).getPropertyValue('--category4-color')
var colordict = {
  "category1": category1_color,
  "category2": category2_color,
  "category3": category3_color,
  "category4": category4_color,


}


function draw_entry(obslist, other){
  var cat = "observation"
  var o = 0.9
  var w = 2.5
  var r = 1.2
  // if other entries
  if (other == true){
    var o = 0.6
    var w = 1.5
    var r = 1
  }
  for (obs in obslist){
    try{
      cat = obslist[obs].category
      var lat = parseFloat(obslist[obs].lat.replace(",","."))
      var lon = parseFloat(obslist[obs].lon.replace(",","."))
      L.circleMarker([lat,lon],
        {
          color: colordict[cat],
          opacity: o,
          radius: r,
          weight: w
        }).addTo(map)
    } catch {
      console.log("error while trying to draw", cat)
    }
  }
}

function draw_entries(){
    draw_entry(category1list,false)
    draw_entry(category2list,false)
    draw_entry(category3list,false)
    draw_entry(category4list,false)
  }


draw_entries()
