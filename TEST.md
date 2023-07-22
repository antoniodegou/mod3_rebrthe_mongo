# Rebrthe Website - Testing

![Mockup](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/mockup.png)


This is the testing portion of reBrthe - the breathing database Website. [Full README available here](README.md) 



The live Website can be found [here](https://rebrthe-flask-mongo.herokuapp.com/).

---

## Table of Contents

 
- [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Linting](#javascript-linting)
    - [Python Linting](#python-linting)
    - [Accessibility Testing](#accessibility)
    - [Performance Testing](#performance)
- [Feature Testing](#feature-testing)
    - [Responsiveness/Device Testing](#responsiveness--device-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Feature Testing Results](#feature-testing-results)
- [User Stories Testing](#user-stories-testing)
- [Bugs and Fixes](#bugs--fixes)


## Validation

### HTML Validation

On the HTML validation, there were no errors.


There were warnings, but they were all related to Bootstrap 5 and how they designed their components. In this instance, the validator pointed out elements inside a  p  tag or  button tag without any text. 

another warning had to do with the <link> tag that Bootstrap gave me the CDN; some fields seem not to be liked by the validator.


![HTML VALID](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/html-valid.png)

---

### CSS Validation

No errors were found on the CSS validator.

![CSS VALID](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/css-valid.png)


---
### JavaScript Linting

No errors were shown in the JS validator. there were a lot of warnings about using the ES6. For example a warning for me using LET/CONST instead of VAR

![JS VALID](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/js-valid.png)

### Python Linting

No errors were found on PEP8 on my Flask app

![PYTHON VALID](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/py-valid.png)



### Accessibility

I use WAVE chrome extension for every page on accessibility. I got no error.  

![ACCESS VALID](https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/wave-valid.png)


| Column 1  | Column 2  |
|:----------|:----------|
| Cell 1    | Cell 2    |



### Performance Testing

All pages were tested with google lighthouse.

<details><summary>HOME ROUTE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-home.png" width="60%">

</details>


<details><summary>PROFILE ROUTE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-profile.png" width="60%">

</details>
 

<details><summary>EXERCISES ROUTE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-exercises.png" width="60%">

</details>

 
<details><summary>PROFILE USER ROUTE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-profile-user.png" width="60%">

</details>

<details><summary>ADMIN ROUTE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-admin.png" width="60%">

</details>



