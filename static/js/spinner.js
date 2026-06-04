// Show the loading spinner when a form with the show-spinner-on-submit class is submitted

document.addEventListener('DOMContentLoaded', function () {
    const spinner = document.getElementById('loading-spinner');
    const forms = document.querySelectorAll('form.show-spinner-on-submit');

    forms.forEach(form => {
        form.addEventListener('submit', function () {
            if (spinner) spinner.classList.remove('d-none');
        });
    });
});