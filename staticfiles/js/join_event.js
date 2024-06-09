// This js allow the user to join and/or leave an event. The counter gets automatically
// updated as the user clicks the buttons. As of now, there is no logic to stop the same user
// from deleting all the participant count or to stop from clicking a million times
// this is definitely a feature to improve
$(document).ready(function() {
    $('#btn-add-participants').click(function() {
        var eventId = $('#btn-add-participants').data('event-id'); // Assuming the event ID is stored as a data attribute

        $.ajax({
            url: `../add-participants/${eventId}`,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                if (response.status === 'success') {
                    $('#participants-number').text(`Number of participants: ${response.participants} `)
                } else {
                    alert('Failed to add participant: ' + response.message);
                }
            }
        });
    });
    $('#btn-remove-participants').click(function() {
        var eventId = $('#btn-remove-participants').data('event-id'); // Assuming the event ID is stored as a data attribute

        $.ajax({
            url: `../remove-participants/${eventId}`,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                if (response.status === 'success') {
                    $('#participants-number').text(`Number of participants: ${response.participants} `)
                } else {
                    alert('Failed to add participant: ' + response.message);
                }
            }
        });
    });
});