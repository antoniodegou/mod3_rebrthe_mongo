// Get all toast elements on the page
const toastElList = [].slice.call(document.querySelectorAll('.toast'));

// Create an array of Bootstrap Toast instances for each toast element
const toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
});

// Show each toast on the page
toastList.forEach(function (toast) {
    toast.show();
});

// Get the current year
const currentYear = new Date().getFullYear();

// Update the copyright year in the footer
document.getElementById("currentYear").innerHTML = `&copy; ${currentYear} reBrthe, Inc`;
