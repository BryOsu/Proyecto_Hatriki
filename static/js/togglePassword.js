document.addEventListener('DOMContentLoaded', function() {
    const togglePassword1 = document.querySelector('#togglePassword1');
    const password1 = document.querySelector('#id_password1');
    const eye1 = document.querySelector('#eye1');

    togglePassword1.addEventListener('click', function () {
        const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
        password1.setAttribute('type', type);
        eye1.classList.toggle('fa-eye-slash');
    });

    const togglePassword2 = document.querySelector('#togglePassword2');
    const password2 = document.querySelector('#id_password2');
    const eye2 = document.querySelector('#eye2');

    togglePassword2.addEventListener('click', function () {
        const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
        password2.setAttribute('type', type);
        eye2.classList.toggle('fa-eye-slash');
    });
});
