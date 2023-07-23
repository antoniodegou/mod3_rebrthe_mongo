let toastElList = [].slice.call(document.querySelectorAll('.toast'));
let toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
});
toastList.forEach(function (toast) {
    toast.show();
});


// Get the current year
const currentYear = new Date().getFullYear();
    
// Update the copyright year in the footer
document.getElementById("currentYear").innerHTML = `&copy; ${currentYear} reBrthe, Inc`;

