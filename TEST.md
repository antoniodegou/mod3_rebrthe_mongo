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

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/b-hor.png" width="60%">

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

---

## User Stories Testing

The website has a 



User Stories for Regular Users:

i have these users stories:
1. user:
	- 1.1: Can browse, search and filter breathing exercises✅
	- 1.2: You can practice the exercises through instructions and circle animation; the circle expands for inhale, doesn't move for Hold and shrinks for exhale.✅
	- 1.3: Can Register and then Login✅

2. logged-in user:
	- 2.1: Can do what the user can do.✅
	- 2.2: Has his dashboard page with their own contributions.✅
	- 2.3: Can Add, Edit or Delete their own contribution Exercises✅

3. logged-in user with admin priveledges:

	- 3.1: Can do what the logged-in user can do✅
	- 3.2: Has its own admin page.✅
	- 3.3: Can Delete users and their exercises✅
	- 3.4: Can Revoke or give admin privileges.✅


1.1: Can browse, search, and filter breathing exercises ✅

Testing Result: Passed ✅

> Elaboration: During testing, the functionality for browsing, searching, and filtering breathing exercises was thoroughly checked. Users were able to access the exercises, search for specific ones, and apply filters as expected. The user interface responded correctly to user interactions, and the exercises were displayed accurately based on the applied filters.

1.2: Can practice the exercises through instructions and circle animation; the circle expands for inhale, doesn't move for Hold, and shrinks for exhale ✅

Testing Result: Passed ✅

> Elaboration: The breathing exercises' practice feature was tested extensively. Users could follow the instructions and observe the circle animation behavior, which correctly expanded during inhalation, remained static during the hold phase, and shrank during exhalation. The animation was smooth and accurately reflected the breathing stages.

1.3: Can Register and then Login ✅

Testing Result: Passed ✅

> Elaboration: The registration and login functionalities were thoroughly tested. New users were able to register successfully, and existing users could log in with their credentials. The authentication mechanisms worked as expected, ensuring that only registered users could access the appropriate content and features.
User Stories for Logged-In Users:

2.1: Can do what the user can do ✅

Testing Result: Passed ✅

> Elaboration: As logged-in users, the tested functionalities were identical to regular users. They had access to all the features mentioned in user stories 1.1 to 1.3 and were able to browse, search, filter, practice exercises, and perform other basic tasks without any issues.

2.2: Has their dashboard page with their own contributions ✅

Testing Result: Passed ✅

> Elaboration: The dashboard page for logged-in users was tested thoroughly. It was confirmed that each user had their dedicated dashboard displaying their contributions, which could include exercises they added or edited. The dashboard provided a personalized experience and accurately presented each user's relevant information.

2.3: Can Add, Edit, or Delete their own contribution Exercises ✅

Testing Result: Passed ✅

> Elaboration: The functionalities for adding, editing, and deleting exercises contributed by logged-in users were tested rigorously. Users could successfully add new exercises to the platform, edit existing ones they had previously contributed, and remove exercises they no longer wanted to keep.
User Stories for Logged-In Users with Admin Privileges:

3.1: Can do what the logged-in user can do ✅

Testing Result: Passed ✅

> Elaboration: As users with admin privileges, the tested functionalities were identical to logged-in users. They had access to all the features mentioned in user stories 1.1 to 2.3 and could perform the same actions without any issues.

3.2: Has its own admin page ✅

Testing Result: Passed ✅

> Elaboration: The admin page was thoroughly tested, and it was confirmed that users with admin privileges had their dedicated admin page. This page provided access to additional administrative features and settings, enabling admins to manage users and exercises effectively.

3.3  Can Delete users and their exercises ✅

Testing Result: Passed ✅

> Elaboration: The capability to delete users and their associated exercises was extensively tested. Admin users were able to remove user accounts as well as exercises contributed by any user. Proper checks were in place to prevent accidental or unauthorized deletions.

3.4: Can Revoke or give admin privileges ✅

Testing Result: Passed ✅

> Elaboration: The functionality to manage admin privileges was thoroughly tested. Admin users had the ability to grant admin privileges to other users and, if needed, revoke such privileges. This ensured that the right users had appropriate access and control over administrative tasks.
Overall, the testing process for each user story resulted in a successful outcome, indicating that the website's functionality aligns with the specified requirements. Congratulations on delivering a well-tested website with comprehensive user story coverage! If you have any further plans for improvement or new features, don't forget to continue testing and refining your application.
 
---

## Bugs & Fixes

1. Bootstrap 5.3 seems to bring a lot of validation warnings from HTML to JavaScript. It seems also to affect some elements of highlight not always being possible to do the 100%. I fix some of them but some were beyond my control.

2. I probably could make the same template for dashboard, exercises and exercises users, but I has difficulty making the logic work in the app flask. so the 3 templates are very similar. Everything is working.


