document.addEventListener('DOMContentLoaded', (event) => {
    console.log('test to check if page is fully loaded');

    // get the button element through the ID assigned in the html
    const joinButton = document.getElementById('join_event');

    joinButton.addEventListener('click', () => {
        console.log('test to check if event listener works')
    });
});