$(document).ready(function() {
    // Get the query string from the URL
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');  // Get the 'search' query parameter

    // Update contents on the page if the search was not Guides 
    if (searchQuery !== "Guides") {
        $("#guide-list").html('<div><h3>No Guides Found!</h3></div>');
        $(".guide-labels").empty();
        $("#pagination-info").text("Search Results: None")
        $("#pagination-list").empty();
    }
});