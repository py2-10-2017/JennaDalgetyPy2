from flask import Flask, redirect, render_template, session, request, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)

app.secret_key = "98efh855v47tybfnu38y"

@app.route("/")

def index():

    return render_template("index.html")


@app.route("/process", methods=["POST", "GET"])

def submit():

    errors = False

    if len(request.form["email"]) < 1:
        flash("Email cannot be blank")
        errors = True
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email Address")
        errors = True
    else:
        session["email"] = request.form["email"]

    if len(request.form["first_name"]) < 1:
        flash("Name cannot be blank")
        errors = True
    elif not request.form["first_name"].isalpha():
        flash("Name cannot contain numbers")
        errors = True
    else:
        session["first_name"] = request.form["first_name"]

    if len(request.form["last_name"]) < 1:
        flash("Name cannot be blank")
        errors = True
    elif not request.form["last_name"].isalpha():
        flash("Name cannot contain numbers")
        errors = True
    else:
        session["last_name"] = request.form["last_name"]

    if len(request.form["password"]) < 8:
        flash("Password must be at least 8 characters in length")
        errors = True
    else:
        session["password"] = request.form["password"]

    if request.form["confirm_password"] != request.form["password"]:
        flash("Passwords must match")
        errors = True
    else:
        session["confirm_password"] = request.form["confirm_password"]

    if errors:
        return redirect("/")
    else:
        flash("Thank you for submitting your information")
        return redirect("/")







app.run(debug=True)