const signinBtn = document.getElementById("signin-button");
const signupBtn = document.getElementById("signup-button");

const signupform = document.getElementById("signup-form");
const signinform = document.getElementById("signin-form");

const homecard = document.getElementById("homecard");
const formcont = document.getElementById("formcont");

homecard.style.transition = "all 0.5s ease";
formcont.style.transition = "all 0.5s ease";

let mBottom = parseInt(window.getComputedStyle(signinform).getPropertyValue('padding'))  
formcont.style.height = signinform.clientHeight +(mBottom  ) + "px" ;
homecard.style.height = signinform.clientHeight  +(mBottom *1.7)   + "px";

signinBtn.addEventListener('click', (e) => {
    e.preventDefault()
 
    mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) *3
    formcont.style.height = signupform.clientHeight   + mBottom  + "px" ;
    homecard.style.height = signupform.clientHeight   +(mBottom *1.7) + "px" ;
    // setTimeout(function() { 
        signupform.classList.add('hiding')
        signinform.classList.remove('hiding')
     
        homecard.style.transition = "all 0.5s ease";
        formcont.style.transition = "all 0.5s ease";
         mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) *3
        formcont.style.height = signinform.clientHeight +mBottom  + "px" ;
        homecard.style.height = signinform.clientHeight  +(mBottom *1.7)   + "px";
    // },200)
})

signupBtn.addEventListener('click', (e) => {
    e.preventDefault()
 
    // signinform.classList.add('do180')
    // homecard.style.transition = "all 1.2s ease";
    // formcont.style.transition = "all 0.5s ease";
    let mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) *3
    formcont.style.height = signupform.clientHeight   + mBottom  + "px" ;
    homecard.style.height = signupform.clientHeight   +(mBottom *1.7) + "px" ;

    // setTimeout(function() { 
        signinform.classList.add('hiding')
        signupform.classList.remove('hiding')
    
    // }, 10)
        // signinform.classList.remove('do180')
        // homecard.style.transition = "all .2s ease";
        // formcont.style.transition = "all .2s ease";
        homecard.style.transition = "all 0.5s ease";
        formcont.style.transition = "all 0.5s ease";
       mBottom = parseInt(window.getComputedStyle(homecard).getPropertyValue('padding-bottom')) *3
        formcont.style.height = signupform.clientHeight   + mBottom  + "px" ;
        homecard.style.height = signupform.clientHeight   +(mBottom *1.7) + "px" ;
    // }, 200)
})

