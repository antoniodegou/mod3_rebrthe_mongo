# Rebrthe

Description: reBrthe is a breathing exercise database that provides users with information and guided practice for various breathing exercises. Users can explore different breathing exercises and practice them with the help of a play button.


![Mockup](readme-img/mockup.jpg)

---

## Table of Contents

- [User Experience (UX)](#user-experience-design)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
  - [Skeleton Plane](#skeleton-plane)
  - [Surface Plane](#surface-plane)
- [Features](#Features)
- [Technologies](#Technologies)
- [Testing](#Testing)
  - [Test Results & Bugs](#test-results--bugs)
- [Deployment](#Deployment)
- [Credits](#Credits)


---

## User Experience Design

### **Strategy Plane**

#### Site Goals

The primary purpose of reBrthe is to provide a central platform for individuals to learn, practice, share and benefit from different breathing exercises. The platform promotes better mental and physical well-being through mindful breathing practices by offering guided activities and information on their benefits.

#### Target Audience

reBrthe is intended for anyone who wants to explore the benefits of various breathing exercises. The platform caters to individuals new to breathing techniques and those seeking to deepen their understanding and practice.

#### User Stories:

All of these apply for new or returning users:

1. user:
	
	- 1.1: Can browse, search and filter breathing exercises
	- 1.2: You can practice the exercises through instructions and circle animation; the circle expands for inhale, doesn't move for Hold and shrinks for exhale.
	- 1.3: Can Register and then Login

2. logged-in user:
	- 2.1: Can do what the user can do.
	- 2.2: Has his dashboard page with their own contributions.
	- 2.3: Can Add, Edit or Delete their own contribution Exercises

3. logged-in user with admin priveledges:

	- 3.1: Can do what the logged-in user can do
	- 3.2: Has its own admin page.
	- 3.3: Can Delete users and their exercises
	- 3.4: Can Revoke or give admin privileges.


---

### **Scope Plane**

**Features planned:**

- General
	- Responsive design
	- MongoDB databases to store breathing exercises and users
		- Exercises: Name, Category, IN, HOLD, OUT, Instructions, Created_by
		- Users: Username, email, password, is_admin
- All users 
	- Navigation
	- Homepage
		- Sign in Form
		- Sign up Form
	- Exercises Page
	- Sign-in Page
	- Sign-up Page

- Signed In users
	- Relevant Homepage (no sign-up on the header)
	- Exercises Page
		- Play/Practice a breathing exercise
	- Dashboard
		- ADD exercise
		- Edit your Own Exercise
		- Delete your Own Exercise
	- Sign Out


- Admin only
	- All signed-in users have
	- Exercises Page
		- Play/Practice a breathing exercise
		- Edit any Exercise
		- Delete any Exercise
	- Admin Page
		- See and sort Users
		- give or take Admin privileges
		- delete users and their library
	- Sign Out

| **User**   | **Feature**                                             | **Difficulty** | **Importance** |
| ---------- | -----------------------------------------------------   | -------------- | -------------- |
| General    | Responsive Design                                       | 2              | 5              |
| General    | MongoDB database to store required data                 | 5              | 5              |
| All Users  | Navigation                                              | 1              | 5              |
| All Users  | Sign In Functionality                                   | 5              | 5              |
| All Users  | Sign Up Functionality                                   | 5              | 5              |
| All Users  | Home Page - branding  (non logged)                      | 1              | 3              |
| All Users  | Custom Error Pages                                      | 1              | 4              |
| All Users  | Practice breathing exercises                            | 4              | 5              |
| Logged  | Same as All users                                          | 0              | 5              |
| Logged  | Home Page - branding     (logged)                          | 1              | 2              |
| Logged  | Sign Out Functionality                                     | 5              | 5              |
| Logged  | Dashboard with CRUD (add, edit or delete own exercises)    | 5              | 5              |
| Logged  | Search by name or description                              | 2              | 3              |
| Logged  | Filter through categories                                  | 2              | 3              |
| Logged  | Practice breathing exercises                               | 4              | 5              |
| Admin  | Same as others                                              | 0              | 5              |
| Admin  | Admin Page                                                  | 1              | 5              |
| Admin  | CRUD on users                                               | 0              | 3             |
| Admin  | Give or revoke admin on users                               | 0              | 3             |
| Admin  | filter on users                                             | 0              | 4             |


	
### **Structure Plane**

Based on the features and the user stories, I developed a flow chart for the site.

![Site Flow Chart](readme-img/planning_flow_diagram.jpg)


These nav links will be displayed based on who the user is and whether they're logged in:


| **Logged Out** | **Logged In (non-admin)** | **Logged In (admin)** |
| -------------- | ------------------------- | --------------------- |
| Home           | Home                      | Home                  |
| Exercises      | Exercises                 | Exercises             |
| Log-in         | --- 					      | ---                   |
| Sign-up        | ---                       | ---                  |
| ---          	  | Dashboard                 |Dashboard          |
| ---            | Logout                    | Logout                |
| ---            | ---                       | Admin            |



1. user:
	
- 1.1: Can browse, search and filter breathing exercises

The site is built with HTML, CSS, JAVASCRIPT; with the help of Bootstrap and a combination of javascript, you can use the select to filter through de diverse categories or use a search field that searches through names and descriptions of each exercise.

It's Responsive for several devices. As a user without an account, I want to understand the site's purpose immediately upon entering.

- 1.2: You can practice the exercises through instructions and circle animation; the circle expands for inhale, doesn't move for Hold and shrinks for exhale.

Each exercise on the reBrthe platform features a "Play" button. A modal window opens when a user clicks this button, presenting a "Play" and "Stop" button inside. The exercise starts by clicking the "Play" button within the modal, allowing the user to practice their breathing. Throughout the exercise, the user receives clear instructions on when to inhale, hold their breath, and exhale, all for a specific and predefined duration. This guided experience enables users to practice mindful breathing, following the structured breathing patterns provided by the platform.


- 1.3: Can Register and then Login


Users can register and login to the reBrthe platform through two convenient access points: the home page header and the top menu, where "Login" and "Sign Up" buttons are available.

2. logged-in user:
	- 2.1: Can do what the user can do.
	- 2.2: Has his dashboard page with their own contributions.
	- 2.3: Can Add, Edit or Delete their own contribution Exercises

Logged-in users enjoy several privileges and functionalities on the reBrthe platform:

Dashboard Page: Users have access to a personalised dashboard that showcases their own contributions.

Add, Edit, or Delete Exercises: On the dashboard page, users can easily add new breathing exercises using the "ADD EXERCISE" button. Each exercise panel also features "EDIT" and "DELETE" buttons, enabling users to modify or remove their own contributions.

Interactive Interface: The dashboard utilises the accordion and modal components from Bootstrap, providing an interactive and user-friendly experience for managing exercises efficiently. The familiar and intuitive interface streamlines the process of creating, editing, and deleting exercises, making it convenient for logged-in users to engage with their contributions.

3. logged-in user with admin priveledges:

	- 3.1: Can do what the logged-in user can do
	- 3.2: Has its own admin page.
	- 3.3: Can Delete users and their exercises
	- 3.4: Can Revoke or give admin privileges.

Logged-in users with admin privileges possess additional capabilities on the reBrthe platform:

Admin Dashboard: An exclusive admin page allows them to manage user-related activities efficiently.

User and Exercise Management: Admins can delete both users and their exercises from the platform.

Admin Privilege Control: They have the authority to grant or revoke admin privileges from other users.

The admin page is thoughtfully designed using Bootstrap's accordion component, facilitating easy navigation and organisation. Admins can sort users by username using the Select component and have a single button to perform the selected action on other users. These features empower admins to maintain the platform effectively and make informed decisions about user management and privileges.


### **Skeleton Plane**

[For wireframes see Surface Plane](#wireframes)

#### Database Design

Mongo Users Collection and Exercises Collection


| **USERS** | **EXERCISES** |  
| -------------- | ------------------------- |  
| _ID          | _ID                    |  
| username  *  | Exercise_name               |  
| email        | Category_name				      |  
| password       | IN                      |  
| is_admin         | HOLD               | 
| ---            | OUT                |  
| ---            | intructions                      | 
| ---            | cycles                     | 
| ---            | created_by   *                   |  

- created_by and username are the same value when talking of a user. * 

- Instruction is a text field for anything from instructions to descriptions.

- Security measures have been implemented for the database connection details in reBrthe:

  - For development purposes, the connection details are set up in an env.py file. To enhance security, this file is not uploaded to GitHub, preventing users from accessing sensitive database information.

  - In production, the database connection details are securely stored in Heroku, ensuring that the information remains protected and not exposed to unauthorised users.

  - By employing these security practices, reBrthe safeguards sensitive data, providing a secure environment for user interactions while protecting confidential database information from potential vulnerabilities.



### **Surface Plane**

#### Wireframes

wireframes were made using Adobe Illustrator.

**Wireframes / Site Design**

<details><summary>HOME</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/home.png" width="80%">

</details>


<details><summary>EXERCISE PAGE , DASHBOARD PAGE and CREATED BY PAGE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/exercises.png" width="80%">

</details>

<details><summary>ADDING MODAL</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/add.png" width="80%">

</details>

<details><summary>EDIT MODAL</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/edit.png" width="80%">

</details>

<details><summary>ADMIN PAGE</summary>

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/admin.png" width="80%">

</details>

#### Design

I chose a very simple design where the main piece is the ever-rotating gradient with a very minimal white and off-black for the content. I use boxes or floating text. 


##### Colour Scheme

I selected four colours and incorporated them into an intricate gradient pattern. Additionally, I utilised a pseudo ::after element, enabling me to amplify the effect by 200% and create a slow, rotating motion, resulting in a pleasing, calming, and hypnotic visual effect.


<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/colours.png" width="80%">

The rest is all black or off-black on top of this colourful background.


##### Typography

I used Satochi in BOLD and Normal for the whole site. Due to its simplistic approach, there was no need for a second font, also due to the fact that Satochi is very versatile. 

<img src="https://raw.githubusercontent.com/antoniodegou/mod3_rebrthe_mongo/main/readme-img/fonts.png" width="80%">

##### Graphics / Imagery

Most of the website is based on its design elements like text, rectangles and circles. But I did use some SVGs bought from freepik.com	to decorate the home page. 



## Features

 
Details of all features on the finished site, expanding on the broader features listed above, including content, functionality & security.

### All Pages (*)

* All elements are adjusted with the help of Bootstrap to any device from mobile to desktop.

* Favicon

* NavBar (responsive)

* Name of the username in Navbar (when logged)

* Footer

* flash message on all moments that are relevant:
	* add exercise
	* edit exercise
	* log in
	* log out
	* delete exercise
	* delete user
	* add/revoke admin priveledges 

### Home (/)

* Header different if logged in or not.

* If not logged in, shows login or sign up in the header.

* Rest of the page is Branding and Information 

* all Responsive from 2 columns to 1 when mobile.

### Exercises (/get_exercises)

* Search button (searches in exercise name and instructions)

* Select Element to help you filter by categories

* Grid with the Breathing Exercises

* Each Breathing Exercise comes with information

	* Play button ( you can practice the exercise)
	* Edit (if admin) you can edit any exercise
	* Delete (if admin) you can delete any exercise
	* A title
	* A category
	* A description/Instructions
	* It part of a bootstrap accordion component
	* A "Made by" field


### Dashboard (only logged in) (/profile/<username>)

* And "add exercise" button
	* It opens a modal where you can fill and add to the database
* Each Breathing Exercise comes with information belonging to logged user

	* Play button ( you can practice the exercise) (opens a modal)
	* Edit you can edit any exercise (opens a modal)
	* Delete you can delete any exercise
	* A title
	* A category
	* A description/Instructions
	* It part of a bootstrap accordion component
	* A "Made by" field

### Admin (only logged in) (/admin/<username>)

* Each Breathing Exercise comes with information belonging to logged user
* An accordion with each user
	* info on the name
	* info on email
	* info on admin rights
	* select three actions
		* revoke admin right
		* give admin rights
		* delete the user and exercise
* a select button so you can filter through users


	
### Login Page and Sign up Page (/register) or (/login)

* fields with validation
* Adds a user to session cookie (log in). Welcomes user with flash message on submission.
* All fields in reBrthe are mandatory, with built-in HTML validation to ensure the correct type, format, and length.
* Username and password are essential fields in reBrthe, and their correctness is enforced. The platform uses Werkzeug's 'check_password_hash' method to safeguard user data, ensuring secure and protected user credentials.

### AUTHOR Page (/profile-user/<username>/<username2>')

* On the Exercise page, usernames serve as clickable links, leading users to view all exercises created by each individual. The page layout follows a template similar to the dashboard, ensuring a familiar and user-friendly experience. This feature empowers users to explore exercises contributed by various authors with ease and convenience.

* username is the user in session

* username 2 is the user being looked at

### The ADD or EDIT MODAL (/profile/<identifier>)

* You don't leave the page When you add or edit and exercise. You get a modal.

* The modal has empty fields in the case of ADD EXERCISE

* The modal fetches the current fields and populates the fields to be edited




