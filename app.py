import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, g)
from flask_pymongo import PyMongo,  ObjectId

from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if  os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.before_request
def before_request():
    # Make the admin and username variables accessible as globals using the g object
    g.admin = False
    g.username = None

    if "user" in session:
        username = mongo.db.users.find_one({"username": session["user"]})["username"]
        selected_username = mongo.db.users.find_one({"username": username})
        g.admin = selected_username.get("is_admin", False)
        g.username = username



@app.route("/")
def get_home():
    admin = g.admin
    username = g.username

    if username:
        return render_template("home.html", username=username, admin=admin)
    else:
        return render_template("home.html", admin=False)


@app.route("/get_exercises")
def get_exercises():
    exercises = list(mongo.db.exercises.find())
    categories = mongo.db.exercises.distinct('category_name')
    

    if "user" in session:
        username = mongo.db.users.find_one({"username": session["user"]})["username"]
        return render_template("exercises.html", exercises=exercises, username=username, categories=categories )
    else:
        return render_template("exercises.html", exercises=exercises, categories=categories)
    

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form["query"]
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    exercises = list(mongo.db.exercises.find({"$text": {"$search": query}}))
    return render_template("exercises.html",  exercises=exercises, username=username)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return handle_register_request()

    return render_template("register.html")


def handle_register_request():
    # check if username already exists in db
    existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

    if existing_user:
        flash("Username already exists")
        return redirect(url_for("register"))

    register = {
        "username": request.form.get("username").lower(),
        "email": request.form.get("email").lower(),
        "password": generate_password_hash(request.form.get("password")),
        "is_admin": False  # Set is_admin to False by default
    }
    mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
    session["user"] = request.form.get("username").lower()
    flash("Registration Successful!")

    # Set the global variables
    g.username = session["user"]
    g.admin = False

    username = g.username
    admin = g.admin

    return render_template("home.html", username=username, admin=admin)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return handle_login_request()

    return render_template("login.html")


def handle_login_request():
    # check if username exists in db
    existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})

    if existing_user:
        # ensure hashed password matches user input
        if check_password_hash(
            existing_user["password"], request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(request.form.get("username")))
            g.username = session["user"]  # Set g.username to the logged-in username
            g.admin = existing_user.get("is_admin", False)  # Set g.admin to the admin status

        else:
            # invalid password match
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    else:
        # username doesn't exist
        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))

    username = g.username
    admin = g.admin

    return render_template("home.html", username=username, admin=admin)

@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    # return render_template("dashboard.html", username=username)
    exercises = mongo.db.exercises.find()
    return render_template("dashboard.html", exercises=exercises, username=username)

@app.route("/admin/<username>", methods=["GET", "POST"])
def admin(username):
    # Check if the user has admin privileges
    user = mongo.db.users.find_one({"username": username, "is_admin": True})

    if user:
        # User has admin privileges, render the admin page
        return render_template("admin.html", username=username)
    else:
        # User does not have admin privileges, redirect to the home page
        return redirect(url_for("get_home"))


@app.route("/profile-user/<username>/<username2>", methods=["GET"])
def profile_user(username, username2):
    # grab the session user's username from db
    session_username = mongo.db.users.find_one({"username": session["user"]})["username"]
    
    # Find the selected user's username from db
    selected_username = mongo.db.users.find_one({"username": username2})
    user_fields = selected_username.keys()
    if selected_username:
        # Retrieve the exercises for the selected user
        exercises = mongo.db.exercises.find({"created_by": username2})
        categories = mongo.db.exercises.distinct('category_name', {"created_by": username2})

        # Render the profile page with the selected user's exercises
        return render_template("exercises-user.html", exercises=exercises, username=session_username, username2=selected_username["username"], categories=categories,  email = selected_username["email"]  )
    else:
        # Handle the case when the selected user is not found
        return render_template("user-not-found.html", username=username2)





@app.route("/profile/<identifier>", methods=["GET", "POST"])
def manage_task(identifier):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if request.method == "POST":
        if identifier == "new":
            # Logic for adding a new task
            task = {
                "exercise_name": request.form.get("exercise_name"),
                "category_name": request.form.get("category_name"),
                "in": request.form.get("in"),
                "hold": request.form.get("hold"),
                "out": request.form.get("out"),
                "instructions": request.form.get("instructions"),
                "cycles": request.form.get("cycles"),
                "created_by": session["user"]
            }
            mongo.db.exercises.insert_one(task)
            flash("Task Successfully Added")
            return redirect(url_for("manage_task", identifier="new"))
        else:
            # Logic for editing an existing task
            submit = {
                "exercise_name": request.form.get("exercise_name"),
                "category_name": request.form.get("category_name"),
                "in": request.form.get("in"),
                "hold": request.form.get("hold"),
                "out": request.form.get("out"),
                "instructions": request.form.get("instructions"),
                "cycles": request.form.get("cycles"),
                "created_by": session["user"]
            }
            mongo.db.exercises.update_one({"_id": ObjectId(identifier)}, {"$set": submit})
            flash("Task Successfully Updated")
            return redirect(url_for("manage_task", identifier=identifier))

    if identifier == "new":
        # Render the page for adding a new task
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("dashboard.html", username=username, identifier="new")
    else:
        # Render the page for editing an existing task
        exercise = mongo.db.exercises.find_one({"_id": ObjectId(identifier)})
        return render_template("dashboard.html", exercise=exercise, username=username, identifier=identifier)


@app.route("/delete_task/<exercise_id>")
def delete_task(exercise_id):
    mongo.db.exercises.delete_one({"_id": ObjectId(exercise_id)})
    flash("Task Successfully Deleted")
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    # return render_template("dashboard.html", username=username)
    exercises = mongo.db.exercises.find()
    return render_template("dashboard.html", exercises=exercises, username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)