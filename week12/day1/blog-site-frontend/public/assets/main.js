$(document).ready(function() {
    $('.js-load-posts').on('click', function() {
        // load the posts into the div with an ID of #posts
    })

    $('.js-new-post-form').on('submit', function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        console.log(formData);
        // send the formData to the server with $.ajax here
    })
})
