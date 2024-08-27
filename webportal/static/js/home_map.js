/* Create a Leaflet map at a certrain view and zoom level. */
var map = L.map('map',{
  // Remove automatic zoom control so we can reposition it freely
  zoomControl:true
}).setView([49, 11.5], 7)

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


  /* Draws the db entries onto the map. */
  function draw_points(dictEntry) {

      /* Because the German decimal point notation (comma vs period)
      we have to replace . and , manually. */
      var lat = parseFloat(dictEntry.lat.replace(",", "."))
      var lon = parseFloat(dictEntry.lon.replace(",", "."))
      try{

           L.circleMarker([lat,lon],
             {
               color: colordict[dictEntry.observation],
               opacity: 0.7,
               fillOpacity: 0.7,
               radius: 2.5,
               weight: 1.2
             }).addTo(map)
         } catch {
           console.log("error while trying to draw", dictEntry.observation)
         }
       }

