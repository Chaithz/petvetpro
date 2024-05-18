document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('appointmentForm');
    const modal = document.getElementById('myModal');
    const fillalert = document.getElementById('myModalalert');
    const closeButton = document.getElementById('closeButton');
    const closeButton2 = document.getElementById('closeButton2');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm()) {
            modal.showModal();
        }
    });

    closeButton.addEventListener('click', function() {
        modal.close();
    });

    closeButton2.addEventListener('click', function() {
        fillalert.close();
    });

    function validateForm() {
        const inputs = form.querySelectorAll('input');
        for (let i = 0; i < inputs.length; i++) {
            if (!inputs[i].value) {
                fillalert.showModal();
               // alert('Please fill in all fields.');
                return false;
            }
        }
        return true;
    }
});

// document.getElementById('appointmentForm').addEventListener('submit', function(event) {
//     event.preventDefault();
//     if (validateForm()) {
//     myModal.showModal();
//     }
// });

// closeButton.addEventListener('click', function(event) {
//     event.preventDefault();
//     myModal.close();
// });

// function validateForm() {
//     const inputs = form.querySelectorAll('input');
//     for (let i = 0; i < inputs.length; i++) {
//         if (!inputs[i].value) {
//             alert('Please fill in all fields.');
//             return false;
//         }
//     }
//     return true;
// }

