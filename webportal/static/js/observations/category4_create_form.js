setupFormBehaviour();

// setup the initial behaviour of the form
function setupFormBehaviour() {
    document.getElementById("id_Certainty_1").checked = true;
    document.getElementById("id_Category4Subject").onchange = () => {
        changeLexiconData(document.getElementById("id_Category4Subject").value)
    }
    document.getElementById("id_Certainty_0").onclick = () => {
        makeLexiconVisible()
    }
    document.getElementById("id_Certainty_1").onclick = () => {
        closeLexicon()
    }
    document.getElementById("id_Photo").onchange = () => {
        readURL(document.getElementById("id_Photo"))
    }
    document.getElementById("div_id_Category4Subject").firstElementChild.innerHTML = '<b>What is the observation about?</b>&nbsp; &nbsp; <img class=\"menu-button\" src=\"/static/image/info_icon_orange.svg\" onclick=\"makeLexiconVisible();\" style=\"float:right;\">';
}

// make the lexicon div visable
function makeLexiconVisible() {
    document.getElementById("Lexicon").style.display = "block";
}

// make the lexicon div invisable
function closeLexicon() {
    document.getElementById("Lexicon").style.display = "none";
}

// fetches the data from the server and stores them into the lexicon div
function changeLexiconData(Category4Subject) {
    fetchLexiconData('category4', Category4Subject).then(function (category4data) {
        document.getElementById('observationtipps').innerText = category4data.Observationtipps
        document.getElementById('observationtime').innerText = category4data.Observationtime

        document.getElementById('subject-name').innerText = category4data.SubjectName
        document.getElementById('subject-latin-name').innerText = category4data.LatinName

        document.getElementById('photo-carousell').innerHTML = makePhotoCarousellHTML(category4data.Photos)
        document.getElementById('home-tab').innerText = category4data.Tabs[0].TabName
        document.getElementById('profile-tab').innerText = category4data.Tabs[1].TabName
        document.getElementById('contact-tab').innerText = category4data.Tabs[2].TabName

        document.getElementById('home').innerHTML = convertListToHTML(category4data.Tabs[0].Content, 'li')
        document.getElementById('profile').innerHTML = convertListToHTML(category4data.Tabs[1].Content, 'li')
        document.getElementById('contact').innerHTML = convertListToHTML(category4data.Tabs[2].Content, 'li')

    }).catch(function () {
        document.getElementById('observationtipps').innerText = ''
        document.getElementById('observationtime').innerText = ''

        document.getElementById('subject-name').innerText = 'Please select first.'
        document.getElementById('subject-latin-name').innerText = ''

        document.getElementById('photo-carousell').innerHTML = ""
        document.getElementById('home-tab').innerText = ''
        document.getElementById('profile-tab').innerText = ''
        document.getElementById('contact-tab').innerText = ''

        document.getElementById('home').innerHTML = ''
        document.getElementById('profile').innerHTML = ''
        document.getElementById('contact').innerHTML = ''
    })
}

function validitychecker(idname, searchword){
var errortextfkt ="";
if (document.getElementById(idname).value == "") {
        errortextfkt = errortextfkt +("Missing " + searchword +" <br>");
        document.getElementById(idname).setCustomValidity('Missing " + searchword +" ');
        document.getElementById(idname).classList.add('is-invalid');
    }else{
        document.getElementById(idname).classList.add('is-valid');
        document.getElementById(idname).setCustomValidity('');
    }
    return errortextfkt
}

function checkformdata(){
    var errortext = "";
    document.getElementById("Errortext_create").innerHTML = errortext;
    var elems = document.querySelectorAll(".is-invalid");
    [].forEach.call(elems, function(el) {el.classList.remove("is-invalid");});
    var elems = document.querySelectorAll(".is-valid");
    [].forEach.call(elems, function(el) {el.classList.remove("is-valid");});

    errortext = errortext + validitychecker("id_Category4Subject", "what is the observation about")
    errortext = errortext + validitychecker("id_Lon", "longitude")
    errortext = errortext + validitychecker("id_Lat", "latitude")
    errortext = errortext + validitychecker("id_ObservationDate", "observation date")

    if (errortext != ""){
        document.getElementById("Errortext_create").innerHTML = errortext;
        return;
    }
    getSpatialInfo();
}