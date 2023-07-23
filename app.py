#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, flash, render_template, redirect, request, \
    session, url_for, g

from flask_pymongo import PyMongo, ObjectId
from bson import ObjectId
from werkzeug.security import generate_password_hash, \
    check_password_hash
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.before_request
def before_request():
    """
    Make the admin and username variables
    accessible as globals using the g object
    """
    g.admin = False
    g.username = None

    if 'user' in session:
        username = mongo.db.users.find_one({'username': session['user'
                                                                ]})['username']
        selected_username = \
            mongo.db.users.find_one({'username': username})
        g.admin = selected_username.get('is_admin', False)
        g.username = username


@app.route('/')
def get_home():
    '''
    Renders home page template
    '''
    admin = g.admin
    username = g.username

    if username:
        return render_template('home.html', username=username,
                               admin=admin)
    else:
        return render_template('home.html', admin=False)


@app.route('/get_exercises')
def get_exercises():
    '''
    Renders the Exercise page
    This all exercises for all users

    '''
    exercises = list(mongo.db.exercises.find())
    categories = mongo.db.exercises.distinct('category_name')

    if 'user' in session:
        username = g.username
        admin = g.admin
        return render_template('exercises.html', exercises=exercises,
                               username=username, admin=admin,
                               categories=categories)
    else:
        return render_template('exercises.html', exercises=exercises,
                               categories=categories)


@app.route('/search', methods=['GET', 'POST'])
def search():
    '''
    Searches within the exercise page
    the name and instrucxtions fields are up for search
    '''
    if request.method == 'POST':
        query = request.form.get('query')
        username = g.username
        admin = g.admin
        exercises = \
            list(mongo.db.exercises.find({'$text': {'$search': query}}))
        return render_template('exercises.html', exercises=exercises,
                               username=username, admin=admin)
    else:
        return redirect(url_for('get_home'))


@app.route('/register', methods=['GET', 'POST'])
def register():

    '''
    Checks if a user is already logged in,
    if so redirects to user profile.
    Renders the sign in page template
    Allows registered users to sign in to their account
    Adds user to session cookie
    Redirects to user profile on submission.
    '''
    if request.method == 'POST':
        return handle_register_request()

    return render_template('register.html')


def handle_register_request():

    # check if username already exists in db

    existing_user = \
        mongo.db.users.find_one({'username': request.form.get('username'
                                                              ).lower()})

    if existing_user:
        flash('Username already exists')
        return redirect(url_for('register'))

    register = {  # Set is_admin to False by default
        'username': request.form.get('username').lower(),
        'email': request.form.get('email').lower(),
        'password': generate_password_hash(request.form.get('password'
                                                            )),
        'is_admin': False,
        }
    mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie

    session['user'] = request.form.get('username').lower()
    flash('Registration Successful!')

    # Set the global variables

    g.username = session['user']
    g.admin = False

    username = g.username
    admin = g.admin

    return render_template('home.html', username=username, admin=admin)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Checks if a user is already logged in,
    Checks username and password
    redirects to login page if any is wrong
    '''
    if request.method == 'POST':
        return handle_login_request()

    return render_template('login.html')


def handle_login_request():

    # check if username exists in db

    existing_user = \
        mongo.db.users.find_one({'username': request.form.get('username'
                                                              ).lower()})

    if existing_user:

        # ensure hashed password matches user input

        if check_password_hash(existing_user['password'],
                               request.form.get('password')):
            session['user'] = request.form.get('username').lower()
            flash('Welcome, {}'.format(request.form.get('username')))
            # Set g.username to the logged-in username
            g.username = session['user']
            # Set g.admin to the admin status
            g.admin = existing_user.get('is_admin', False)
        else:

            # invalid password match

            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))
    else:

        # username doesn't exist

        flash('Incorrect Username and/or Password')
        return redirect(url_for('login'))

    username = g.username
    admin = g.admin

    return render_template('home.html', username=username, admin=admin)


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    if 'user' in session:
        logged_in_username = g.username
        admin = g.admin
        exercises = mongo.db.exercises.find()
        return render_template('dashboard.html', exercises=exercises,
                               username=logged_in_username, admin=admin)
    else:
        return redirect(url_for('login'))


@app.route('/admin/<username>', methods=['GET', 'POST'])
def admin(username):

    # Check if the user has admin privileges

    user = mongo.db.users.find_one({'username': username,
                                   'is_admin': True})

    if user:
        if request.method == 'POST':
            return handle_admin_request()
        """
        User has admin privileges, retrieve all
        users except the user in session
        """
        users = \
            list(mongo.db.users.find({'username': {'$ne': session['user'
                                                                  ]}}))
        exercises_count = []

        for user in users:
            exercise_count = \
                mongo.db.exercises.count_documents(
                    {'created_by': user['username']})
            exercises_count.append({'username': user['username'],
                                   'count': exercise_count})

        return render_template('admin.html', username=username,
                               users=users,
                               exercises_count=exercises_count,
                               admin=user)
    else:

        # User does not have admin privileges, redirect to the home page

        return redirect(url_for('get_home'))


def handle_admin_request():
    action = request.form.get('action')
    user_id = request.form.get('user_id')

    if action == 'delete':

        # Retrieve the username of the user being deleted

        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        username = user['username']

        # Delete user and their exercises

        mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        mongo.db.exercises.delete_many({'created_by': username})
        flash('User and associated exercises deleted successfully.')
    elif action == 'grant_admin':

        # Grant admin privileges to the user

        mongo.db.users.update_one({'_id': ObjectId(user_id)},
                                  {'$set': {'is_admin': True}})
        flash('Admin privileges granted to the user.')
    elif action == 'revoke_admin':

        # Revoke admin privileges from the user

        mongo.db.users.update_one({'_id': ObjectId(user_id)},
                                  {'$set': {'is_admin': False}})
        flash('Admin privileges revoked from the user.')
    else:
        flash('Invalid action.')

    return redirect(url_for('admin', username=g.username))


@app.route('/profile-user/<username>/<username2>', methods=['GET'])
def profile_user(username, username2):
    if 'user' in session:
        session_username = g.username
        admin = g.admin

        selected_username = \
            mongo.db.users.find_one({'username': username2})
        if selected_username:
            exercises = \
                mongo.db.exercises.find({'created_by': username2})
            categories = mongo.db.exercises.distinct(
                'category_name', {'created_by': username2})
            email = selected_username.get('email')
            return render_template(
                'exercises-user.html',
                exercises=exercises,
                username=session_username,
                username2=selected_username['username'],
                categories=categories,
                email=email,
                admin=admin,
                )
        else:
            return render_template('404.html',
                                   username=username2)
    else:
        return redirect(url_for('login'))


@app.route('/profile/<identifier>', methods=['GET', 'POST'])
def manage_task(identifier):
    """
    edit and add task on the same page
    you choose add and edit
    """
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']

    if request.method == 'POST':
        if identifier == 'new':

            # Logic for adding a new task

            task = {
                'exercise_name': request.form.get('exercise_name'),
                'category_name': request.form.get('category_name'),
                'in': request.form.get('in'),
                'hold': request.form.get('hold'),
                'out': request.form.get('out'),
                'instructions': request.form.get('instructions'),
                'cycles': request.form.get('cycles'),
                'created_by': session['user'],
                }
            mongo.db.exercises.insert_one(task)
            flash('Task Successfully Added')
            return redirect(url_for('manage_task', identifier='new'))
        else:

            # Logic for editing an existing task

            submit = {
                'exercise_name': request.form.get('exercise_nameE'+identifier),
                'category_name': request.form.get('category_nameE'+identifier),
                'in': request.form.get('inE'+identifier),
                'hold': request.form.get('holdE'+identifier),
                'out': request.form.get('outE'+identifier),
                'instructions': request.form.get('instructionsE'+identifier),
                'cycles': request.form.get('cyclesE'+identifier),
                'created_by': session['user'],
                }
            mongo.db.exercises.update_one({'_id': ObjectId(identifier)},
                                          {'$set': submit})
            flash('Task Successfully Updated')
            return redirect(url_for('manage_task',
                            identifier=identifier))

    if identifier == 'new':

        # Render the page for adding a new task
        return render_template('dashboard.html', username=username,
                               identifier='new')
    else:

        # Render the page for editing an existing task

        exercise = \
            mongo.db.exercises.find_one({'_id': ObjectId(identifier)})
        return render_template('dashboard.html', exercise=exercise,
                               username=username, identifier=identifier)


@app.route('/delete_task/<exercise_id>')
def delete_task(exercise_id):
    """
    Get the exercise id
    deletes the records
    """
    mongo.db.exercises.delete_one({'_id': ObjectId(exercise_id)})
    flash('Task Successfully Deleted')
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']

    # return render_template("dashboard.html", username=username)

    exercises = mongo.db.exercises.find()
    return render_template('dashboard.html', exercises=exercises,
                           username=username)


@app.route('/logout')
def logout():

    # remove user from session cookie

    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    '''
    Renders custom 404 page
    '''
    return render_template("404.html", error=error), 404


@app.errorhandler(500)
def internal_error(error):
    '''
    Renders custom 500 page
    '''
    return render_template("500.html", error=error), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=False)
