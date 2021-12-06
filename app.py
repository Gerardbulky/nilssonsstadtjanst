import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# mail starts here
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_HOST_USER'] = os.environ.get("MAIL_HOST_USER")
app.config['MAIL_PASS'] = os.environ.get("MAIL_PASS")
# app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("MAIL_HOST_USER")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mail = Mail(app)
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


@app.route("/sendmail")
def sendmail():
    
    return render_template("sendmail.html")


@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find().sort("_id", -1)) # i made task into list to get the length
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    return render_template("tasks.html", tasks=tasks, date_time=date_time, time=time)



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    if not tasks:
        flash("Du har angett ett felaktigt sökkriterium")
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
            flash("Användarnamn existerar redan.")
            return redirect(url_for('create_account'))

        if password == confirm:
            create_account = {"username": username,
                              "password": generate_password_hash(password)} 
            mongo.db.users.insert_one(create_account) 
            
        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registrering lyckad!")
            return redirect(url_for('profile', username=session["user"]))
        else:
            flash("Lösenordet matchar inte.")

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
                flash("Felaktigt användarnamn och/eller lösenord.")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Felaktigt användarnamn och/eller lösenord.")
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
        return redirect(url_for("get_tasks"))
        # return render_template("profile.html", username=username, categories=categories, task=task)
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
        if "user" in session:
            task = {
                "category_name": request.form.get("category_name"),
                "any_additional_information": request.form.get("any_additional_information"),
                "time_and_date": request.form.get("time_and_date"),
                "address": request.form.get("address"),
                "phone_number": request.form.get("phone_number"),
                "email": request.form.get("email"),
                "home_size": request.form.get("home_size"),
                "full_name": request.form.get("full_name"),
                "window_type_one": request.form.get("window_type_one"),
                "window_count_one": request.form.get("window_count_one"),
                "window_type_two": request.form.get("window_type_two"),
                "window_count_two": request.form.get("window_count_two"),
                "window_type_three": request.form.get("window_type_three"),
                "window_count_three": request.form.get("window_count_three"),
                "window_cleaning_sides": request.form.get("window_cleaning_sides"),
                "myFile": request.form.get("myFile"),
                "created_by": session["user"]
            }
            mongo.db.tasks.insert_one(task)
            flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
            return redirect(url_for("profile", username=session["user"]))
        else:
            task = {
                "category_name": request.form.get("category_name"),
                "any_additional_information": request.form.get("any_additional_information"),
                "time_and_date": request.form.get("time_and_date"),
                "address": request.form.get("address"),
                "phone_number": request.form.get("phone_number"),
                "email": request.form.get("email"),
                "home_size": request.form.get("home_size"),
                "full_name": request.form.get("full_name"),
                "window_type_one": request.form.get("window_type_one"),
                "window_count_one": request.form.get("window_count_one"),
                "window_type_two": request.form.get("window_type_two"),
                "window_count_two": request.form.get("window_count_two"),
                "window_type_three": request.form.get("window_type_three"),
                "window_count_three": request.form.get("window_count_three"),
                "window_cleaning_sides": request.form.get("window_cleaning_sides"),
                "myFile": request.form.get("myFile"),
                
            }
            mongo.db.tasks.insert_one(task)
            flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
            return redirect(url_for("index"))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("add_task.html", categories=categories)


@app.route("/home_visit", methods=["GET", "POST"])
def home_visit():
    if request.method == "POST":
        if "user" in session:
            visit = {
                "category_name": request.form.get("category_name"),
                "time_and_date": request.form.get("time_and_date"),
                "address": request.form.get("address"),
                "phone_number": request.form.get("phone_number"),
                "email": request.form.get("email"),
                "full_name": request.form.get("full_name"),
                "created_by": session["user"]
            }
            mongo.db.tasks.insert_one(visit)
            flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
            return redirect(url_for("profile", username=session["user"]))
        else:
            visit = {
                "category_name": request.form.get("category_name"),
                "time_and_date": request.form.get("time_and_date"),
                "address": request.form.get("address"),
                "phone_number": request.form.get("phone_number"),
                "email": request.form.get("email"),
                "full_name": request.form.get("full_name"),
            }
            mongo.db.tasks.insert_one(visit)
            flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
            return redirect(url_for("index"))
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
            "email": request.form.get("email"),
            "myFile": request.form.get("myFile"),
            "home_size": request.form.get("home_size"),
            "full_name": request.form.get("full_name"),
            "window_type_one": request.form.get("window_type_one"),
            "window_count_one": request.form.get("window_count_one"),
            "window_type_two": request.form.get("window_type_two"),
            "window_count_two": request.form.get("window_count_two"),
            "window_type_three": request.form.get("window_type_three"),
            "window_count_three": request.form.get("window_count_three"),
            "window_cleaning_sides": request.form.get("window_cleaning_sides"),
            "any_additional_information": request.form.get("any_additional_information"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(window)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("window_booking.html", categories=categories)


@app.route("/home_booking", methods=["GET", "POST"])
def home_booking():
    if request.method == "POST":
        home = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(home)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("home_booking.html", categories=categories)


@app.route("/big_booking", methods=["GET", "POST"])
def big_booking():
    if request.method == "POST":
        big = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(big)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("big_booking.html", categories=categories)


@app.route("/step_booking", methods=["GET", "POST"])
def step_booking():
    if request.method == "POST":
        step = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"), 
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(step)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("step_booking.html", categories=categories)


@app.route("/company_booking", methods=["GET", "POST"])
def company_booking():
    if request.method == "POST":
        company = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"), 
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(company)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("company_booking.html", categories=categories)


@app.route("/moving_booking", methods=["GET", "POST"])
def moving_booking():
    if request.method == "POST":
        moving = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"), 
            "home_size": request.form.get("home_size"),
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(moving)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("moving_booking.html", categories=categories)


@app.route("/office_booking", methods=["GET", "POST"])
def office_booking():
    if request.method == "POST":
        office = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"), 
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(office)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("office_booking.html", categories=categories)


@app.route("/boutique_booking", methods=["GET", "POST"])
def boutique_booking():
    if request.method == "POST":
        boutique = {
            "category_name": request.form.get("category_name"),
            "time_and_date": request.form.get("time_and_date"),
            "address": request.form.get("address"), 
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "full_name": request.form.get("full_name"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(boutique)
        flash("Tack för bokningen!. Uppgiften har lagts till. Vi hör av oss.")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)    
    return render_template("boutique_booking.html", categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted.")
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
        flash("New Category Added.")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated.")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted.")
    return redirect(url_for("get_categories"))


if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)