function getPolyList(polyLayer,t, p){
  var polyList = []
  polyLayer.eachLayer(
    function(layer) {
      if (layer.feature.properties[p] != undefined && layer.feature.properties[p].includes(t)){
        polyList.push(layer)
      }

    }
  )
  return polyList
}

function spatialPreSelection_Montain(lng){
  if (lng <= 11.5){// select only western mountain ranges
    return "w"
  }else{ // select only eastern mountain ranges
    return "e"}
}


  /* Preselect region to speed marker search in polygon up. This is relevant
   for the municipalities. */
  function spatialPreSelection_Bavaria(lat,lng){
    var tiles = [
      ["t01","t05", null , "t14"],
      ["t02","t06", "t10" , "t15"],
      ["t03","t07", "t11" , "t16"],
      ["t04","t08", "t12" , "t17"],
      [null,"t09", "t13" , "t18"],
    ]

    y_index = 0
    x_index = 0
    if (lat >= 49.82075){
      y_index = 0
    } else if (lat >= 48.82075){
      y_index = 1
    } else if (lat >= 47.82075){
      y_index = 2
    } else if (lat >= 46.82075){
      y_index = 3
    }

    if (lng <= 9.891){
      x_index = 0
    } else if (lng <= 10.891){
      x_index = 1
    } else if (lng <= 11.891){
      x_index = 2
    } else if (lng <= 12.891){
      x_index = 3
    } else if (lng <= 13.891){
      x_index = 4
    }

    var tile = tiles[x_index][y_index]
    /* Returns a tile/grid cell name which intersects the polygons. */
    return tile
  }
