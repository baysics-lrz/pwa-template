setupFormBehaviour();

// setup the initial behaviour of the form
function setupFormBehaviour() {
    document.getElementById("id_Certainty_1").checked = true;
    document.getElementById("id_Category3Subject").onchange = () => {
        changeLexiconData(document.getElementById("id_Category3Subject").value)
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
    document.getElementById("div_id_Category3Subject").firstElementChild.innerHTML = '<b>What is the observation about?</b>&nbsp; &nbsp; <img class=\"menu-button\" src=\"/static/image/info_icon_orange.svg\" onclick=\"makeLexiconVisible();\" style=\"float:right;\">';

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

    errortext = errortext + validitychecker("id_Category3Subject", "what is the observation about")
    errortext = errortext + validitychecker("id_Lon", "longitude")
    errortext = errortext + validitychecker("id_Lat", "latitude")
    errortext = errortext + validitychecker("id_ObservationDate", "observation date")
    errortext = errortext + validitychecker("id_Photo", "image")
    if(!document.getElementById('id_Category3Feature1_0').checked && !document.getElementById('id_Category3Feature1_1').checked && !document.getElementById('id_Category3Feature1_2').checked){
        errortext = errortext +("Missing feature1<br>");
        document.getElementById('id_Category3Feature1_0').classList.add('is-invalid');
        document.getElementById('id_Category3Feature1_1').classList.add('is-invalid');
        document.getElementById('id_Category3Feature1_2').classList.add('is-invalid');
        // color radio buttons that are empty but required
        document.getElementById('div_id_Category3Feature1').style.color = "red"
    }else{
        document.getElementById('id_Category3Feature1_0').classList.add('is-valid');
        document.getElementById('id_Category3Feature1_1').classList.add('is-valid');
        document.getElementById('id_Category3Feature1_2').classList.add('is-valid');
        document.getElementById('div_id_Category3Feature1').style.color = "#24435a"
    }
    errortext = errortext + validitychecker("id_Category3Feature2", "feature2")
    if (errortext != ""){
        document.getElementById("Errortext_create").innerHTML = errortext;
        return;
    }
    getSpatialInfo();
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
function changeLexiconData(Category3Subject) {
    fetchLexiconData('category3', Category3Subject).then(function (category3data) {
        document.getElementById('observationtipps').innerText = category3data.Observationtipps
        document.getElementById('observationtime').innerText = category3data.Observationtime

        document.getElementById('subject-name').innerText = category3data.SubjectName
        document.getElementById('subject-latin-name').innerText = category3data.LatinName

        document.getElementById('photo-carousell').innerHTML = makePhotoCarousellHTML(category3data.Photos)
        document.getElementById('home-tab').innerText = category3data.Tabs[0].TabName
        document.getElementById('profile-tab').innerText = category3data.Tabs[1].TabName
        document.getElementById('contact-tab').innerText = category3data.Tabs[2].TabName

        document.getElementById('home').innerHTML = convertListToHTML(category3data.Tabs[0].Content, 'li')
        document.getElementById('profile').innerHTML = convertListToHTML(category3data.Tabs[1].Content, 'li')
        document.getElementById('contact').innerHTML = convertListToHTML(category3data.Tabs[2].Content, 'li')

    }).catch(function () {
        document.getElementById('observationtipps').innerText = ''
        document.getElementById('observationtime').innerText = ''

        document.getElementById('subject-name').innerText = 'Bitte select first.'
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
