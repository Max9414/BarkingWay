$(document).ready(function() {
    $('#createLocationButton').click(function(event) {
        console.log('Button clicked!');
        event.preventDefault(); 

        $.ajax({
            type: 'POST',
            url: 'create-location/', 
            data: $(this).serialize(), 
            success: function(response) {
                // Handle successful response from the server
                alert('Location added successfully!');
            },
            error: function(xhr, errmsg, err) {
                // Handle errors
                console.log(xhr.status + ": " + xhr.responseText); // Log error message
            }
        });
    });
});