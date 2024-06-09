// This js allow the user to join and/or leave an event. The counter gets automatically
// updated as the user clicks the buttons. As of now, there is no logic to stop the same user
// from deleting all the participant count or to stop from clicking a million times
// this is definitely a feature to improve
$(document).ready(function() {
    function showModal(message) {
        $('#modalText').text(message);
        $('#successModal').modal('show');
    }

    $('#modalOkButton').click(function() {
        $('#successModal').modal('hide');
        window.location.reload();
    });

    $('#successModal').on('hidden.bs.modal', function () {
        window.location.reload();
    });

    $('#btn-add-participants').click(function() {
        var eventId = $(this).data('event-id');

        $.ajax({
            url: `../add-participants/${eventId}`,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                if (response.status === 'success') {
                    showModal('You joined the walk! Press OK to reload.');
                } else {
                    alert('Failed to add participant: ' + response.message);
                }
            }
        });
    });

    $('#btn-remove-participants').click(function() {
        var eventId = $(this).data('event-id');

        $.ajax({
            url: `../remove-participants/${eventId}`,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                if (response.status === 'success') {
                    showModal('You left the walk! Press OK to reload.');
                } else {
                    alert('Failed to remove participant: ' + response.message);
                }
            }
        });
    });
});