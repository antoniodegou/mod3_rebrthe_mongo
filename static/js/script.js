// Get references to various elements in the HTML document using their IDs.
const signinBtn = document.getElementById("signin-button");
const signupBtn = document.getElementById("signup-button");
const signupform = document.getElementById("signup-form");
const signinform = document.getElementById("signin-form");
const homecard = document.getElementById("homecard");
const formcont = document.getElementById("formcont");

// Set CSS transitions for smoother animations when changing element styles.
homecard.style.transition = "all 0.5s ease";
formcont.style.transition = "all 0.5s ease";

// Calculate the vertical padding (marginBottom) of the 'signin-form' element
// and adjust the 'formcont' and 'homecard' heights accordingly.
let mBottom = parseInt(window.getComputedStyle(signinform).getPropertyValue('padding'));
formcont.style.height = signinform.clientHeight + (mBottom) + "px";
homecard.style.height = signinform.clientHeight + (mBottom * 1.7) + "px";

// Add a click event listener to the 'signinBtn' element.
signinBtn.addEventListener('click', (e) => {
    // Prevent the default click behavior (e.g., form submission, page reload).
    e.preventDefault();

    // Recalculate the vertical padding (marginBottom) of the 'homecard' element to resize it.
    mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) * 3;

    // Adjust the 'formcont' and 'homecard' heights to match the 'signupform' height with the new padding.
    formcont.style.height = signupform.clientHeight + mBottom + "px";
    homecard.style.height = signupform.clientHeight + (mBottom * 1.7) + "px";

    // Hide the 'signupform' by adding the 'hiding' class and show the 'signinform' by removing the 'hiding' class.
    signupform.classList.add('hiding');
    signinform.classList.remove('hiding');

    // Set CSS transitions for smoother animations when changing element styles.
    homecard.style.transition = "all 0.5s ease";
    formcont.style.transition = "all 0.5s ease";

    // Recalculate the vertical padding (marginBottom) of the 'homecard' element after the class change.
    mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) * 3;

    // Adjust the 'formcont' and 'homecard' heights again to accommodate the 'signinform' height with the new padding.
    formcont.style.height = signinform.clientHeight + mBottom + "px";
    homecard.style.height = signinform.clientHeight + (mBottom * 1.7) + "px";
});

// Add a click event listener to the 'signupBtn' element.
signupBtn.addEventListener('click', (e) => {
    // Prevent the default click behavior (e.g., form submission, page reload).
    e.preventDefault();

    // Calculate the vertical padding (marginBottom) of the 'homecard' element to resize it.
    let mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) * 3;

    // Adjust the 'formcont' and 'homecard' heights to match the 'signupform' height with the new padding.
    formcont.style.height = signupform.clientHeight + mBottom + "px";
    homecard.style.height = signupform.clientHeight + (mBottom * 1.7) + "px";

    // Hide the 'signinform' by adding the 'hiding' class and show the 'signupform' by removing the 'hiding' class.
    signinform.classList.add('hiding');
    signupform.classList.remove('hiding');

    // Set CSS transitions for smoother animations when changing element styles.
    homecard.style.transition = "all 0.5s ease";
    formcont.style.transition = "all 0.5s ease";

    // Recalculate the vertical padding (marginBottom) of the 'homecard' element after the class change.
    mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) * 3;

    // Adjust the 'formcont' and 'homecard' heights again to accommodate the 'signupform' height with the new padding.
    formcont.style.height = signupform.clientHeight + mBottom + "px";
    homecard.style.height = signupform.clientHeight + (mBottom * 1.7) + "px";
});
