import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/moving_cleaning")
def moving_cleaning():
    return render_template("moving_cleaning.html")


@app.route("/home_cleaning")
def home_cleaning():
    return render_template("home_cleaning.html")


@app.route("/company_cleaning")
def company_cleaning():
    return render_template("company_cleaning.html")


@app.route("/window_cleaning")
def window_cleaning():
    return render_template("window_cleaning.html")


@app.route("/step_cleaning")
def step_cleaning():
    return render_template("step_cleaning.html")


@app.route("/office_cleaning")
def office_cleaning():
    return render_template("office_cleaning.html")


@app.route("/big_cleaning")
def big_cleaning():
    return render_template("big_cleaning.html")


@app.route("/boutique_cleaning")
def boutique_cleaning():
    return render_template("boutique_cleaning.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/discount")
def discount():
    return render_template("discount.html")


@app.route("/prices")
def prices():
    return render_template("prices.html")


@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find().sort("_id", -1)
    return render_template("tasks.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)



@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for('create_account'))

        if password == confirm:
            create_account = {"username": username,
                        "password": generate_password_hash(password)} 
            mongo.db.users.insert_one(create_account) 
            
        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for('profile', username=session["user"]))
        else:
            flash("Passwords do not match.")

    return render_template("create_account.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for('profile', username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")
    

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # grapping the session user's username from db
    categories = mongo.db.categories.find()
    task = mongo.db.tasks.find().sort("_id", -1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if "user" in session:
        return render_template("profile.html", username=username, categories=categories, task=task)
       
    return render_template(url_for('login'))

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = {
            "category_name": request.form.get("category_name"),
            "any_additional_information": request.form.get("any_additional_information"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"),
            "how_often": request.form.get("how_often"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("add_task.html", categories=categories)


@app.route("/home_visit", methods=["GET", "POST"])
def home_visit():
    if request.method == "POST":
        visit = {
            "category_name": request.form.get("category_name"),
            "any_additional_information": request.form.get("any_additional_information"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(visit)
        flash("Task Successfully Added")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("home_visit.html", categories=categories)


@app.route("/window_booking", methods=["GET", "POST"])
def window_booking():
    if request.method == "POST":
        window = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(window)
        flash("Task Successfully Added")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("window_booking.html", categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/get_categories")
def get_categories():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)