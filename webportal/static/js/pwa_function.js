function pwafunction() {
        var x = document.getElementById("pwa-banner");

        if (x.style.display === "none") {
            x.style.display = "block";
        } else {
            x.style.display = "none";
        }
        var style = x.style.display;
        var today = new Date().getTime() + (24 * 60 * 60 * 1000);


        if (window.localStorage) {

            localStorage.setItem("savedstyle", style);
            localStorage.setItem("savedtime", today);
            console.log("saved value " + localStorage.savedstyle);
            console.log("saved time " + localStorage.savedtime);
        } else {
            // Sorry!! no Web Storage support..
        }
    }



