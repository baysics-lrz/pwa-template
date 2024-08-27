function showhide(showhidediv) {
  var x = document.getElementById(showhidediv);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function openNav() {
  document.getElementById("myNav").style.height = "100%";
  document.getElementById("nav-open").style.display = "none";
  document.getElementById("nav-close").style.display = "block";
}

function closeNav() {
  document.getElementById("myNav").style.height = "0%";
  document.getElementById("nav-open").style.display = "block";
  document.getElementById("nav-close").style.display = "none";
}

function openBeobErkl() {
    document.getElementById("ObservationsInfo").style.display="block";
    document.getElementsByClassName('observationbanner')[0].style.display="none";
    console.log("Test");
}
function closeBeobErkl() {
    document.getElementById("ObservationsInfo").style.display="none";
    document.getElementsByClassName('observationbanner')[0].style.display="block";
}


function displayDetailSubject(showArt){
    var g = document.getElementsByClassName("showentry");
    for (i = 0; i < g.length; i++) {
        g[i].style.display = "none";
    }
    if (showArt!="nichts"){
    document.getElementById(showArt).style.display = "block";
    }
}

function displayWindowSize(){
    // Get width and height of the window excluding scrollbars
    var schwelle1=470;
    var schwelle2=767;
    var walt =document.getElementById("divWidth").innerHTML;

    var w = document.documentElement.clientWidth;
    if ((walt<schwelle1 && w>schwelle1)||(walt<schwelle2 && w>schwelle2)||(walt>schwelle1 && w<schwelle1)||(walt>schwelle2 && w<schwelle2))
    closeNav();


    // Display result inside a div element
    document.getElementById("divWidth").innerHTML =  w;
}
// Attaching the event listener function to window's resize event
window.addEventListener("resize", displayWindowSize);
// Calling the function for the first time
displayWindowSize();