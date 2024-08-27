$(document).ready(function() {
    $("#show_hide_password a").on('click', function(event) {
        event.preventDefault();
        if($('#show_hide_password input').attr("type") == "text"){
            $('#show_hide_password input').attr('type', 'password');
            $('#show_hide_password i').addClass( "fa-eye-slash" );
            $('#show_hide_password i').removeClass( "fa-eye" );
        }else if($('#show_hide_password input').attr("type") == "password"){
            $('#show_hide_password input').attr('type', 'text');
            $('#show_hide_password i').removeClass( "fa-eye-slash" );
            $('#show_hide_password i').addClass( "fa-eye" );
        }
    });
    var result = detect.parse(navigator.userAgent);
    var note=0;
    console.log("You are using " + result.browser.family +" v" + result.browser.version + " on " + result.os.family);
    if (result.browser.family == "Firefox" && result.browser.version > 50) note =1;
    if (result.browser.family == "Chrome" && result.browser.version > 60) note =1;
    if (result.browser.family == "Edge" && result.browser.major > 10) note =1;
    if (result.browser.family == "Opera" && result.browser.major > 60) note =1;
    if (result.browser.family == "Mobile Safari" && result.browser.major > 11) note =1;
    if (result.browser.family == "Chrome Mobile" && result.browser.major > 60) note =1;
    console.log(note);
    if (note < 1){
        document.getElementById('Warning').innerHTML = "&#x26A0;Attention, compatibility cannot be guaranteed for your browser!";
    }

});