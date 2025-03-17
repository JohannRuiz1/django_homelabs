$(document).ready(function(event){
    function goToLink(event){
        window.location.href = event.data.link;
    }

    // HTML validation said <a> around buttons is bad, so using this 
    $("#guide-btn").on( "click", {link: "list.html?search=Guides"}, goToLink);

    $("#login-btn").on( "click", {link: "login.html"}, goToLink);

    $("#add-suggestion-btn").on( "click", {link: "suggestion-guide.html"}, goToLink);

    $("#save-suggestion-btn").on( "click", {link: "guide.html"}, goToLink);

});