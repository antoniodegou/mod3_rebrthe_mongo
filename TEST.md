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

 

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/wave-valid.png" width="60%">


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

### Tools for testing 🛠

1. Macbook pro m1 2021
2. Google Chrome
3. firefox
4. Safari
5. Hoverify (emulates an Extensive Mobile devices list)
6. Google Dev Tools
7. Huawei Mate 20
8. iMac 2019

### Responsiveness

I used Hoverify, which allows me to test several devices simultaneously in live time.

<details><summary>Horizontal</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/test-hor.png" width="60%">

</details>

<details><summary>Vertical</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/b-ver.png" width="60%">

</details>

### Browser compatibility


### Feature Testing 🚦


##### All pages

1. Nav links working (pass)✅
2. Nav dynamic links according to the logged or unlogged user (pass)✅
3. Nav Responsive (pass)✅
4. Footer links working (pass)✅
5. Footer dynamic links according to the logged or unlogged user (pass)✅
6. Footer Responsive (pass)✅
7. have a logo with the name of the logged user in the nav (pass)✅
8. responsive for all devices (pass)✅
9. background complex gradient animation rotation (pass)✅

##### HOME


1. show written contents and image (pass)✅
2. Show different headers for logged and unlogged users 
	1. Have log-in and sign-up forms for unlogged users  ✅
	2. Show animation for logged users  ✅

##### EXERCISES (all exercises)  

1. Show all exercises by all users (pass)✅
2. Search button looking over title and instructions (pass)✅
3. show in all exercises 
	1. title✅
	2. creator✅
	3. exercises timings✅
	4. category✅
	5. play button✅
		1. star exercises button  ✅
		2. opens in a modal  ✅
		3. working stop button  ✅
		4. Able to load the times and little of selected exercise ✅
		5. darker colour modal  ✅
	6. delete button (only if admin)✅
	7. description✅
4. Select component that you can filter categories(pass) ✅


##### EXERCISES (when you click on a user )
1. the same as the exercises page ✅
2. filter the chosen user exercises ✅
3. delete exercise (only for admin) ✅
4. no edit button ✅
5. no username ( because its all by the same) ✅

##### DASHBOARD (profile)

1. show logged user title (pass)✅
2. show exercises just by the logged user (pass) ✅
3. show in all exercises:
	1. same as the "All exercises" (pass)  ✅
	2. Edit button
		1. Load the info on the exercise in all fields  ✅
		2. save the edited record when pressing the button  ✅
		3. edit appears in modal. ✅
		4. darker colour modal.  ✅

##### ADMIN

1. Show only when admin privileges  ✅
2. Show a card per user.
3. Select component where you can filter by user. 
4.  Card information
	1. username ✅
	2. email ✅
	3. admin privileges  ✅
	4. number of exercises the user has  ✅
	5. working perform action button  ✅
	6. select component with three actions:
		1. revoke privileges  ✅
		2. attributes privileges  ✅
		3. delete user and exercises ✅
5. Title with updated admin user name  ✅



		
