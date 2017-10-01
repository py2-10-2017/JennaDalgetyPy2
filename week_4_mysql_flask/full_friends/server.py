from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, url_for, session
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "iwb38y4938vy3u4ir"
mysql = MySQLConnector(app, "full_friends")



@app.route("/")
def index():

    success_query = "SELECT * FROM users"

    query_results = mysql.query_db(success_query)

    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("index.html", messages = flash_messages, styles = staticfile)



@app.route("/friends", methods=["POST"])
def create():

    print("in create route")

    errors = []

    if not EMAIL_REGEX.match(request.form["email"]):
        errors.append("Email is not valid!")
    if len(request.form["email"]) < 1:
        errors.append("Email is not valid")

    if len(request.form["first_name"]) < 1:
        errors.append("Must enter a first name")
    elif not request.form["first_name"].isalpha():
        errors.append("Name cannot contain numbers")

    if len(request.form["last_name"]) < 1:
        errors.append("Must enter a last name")
    elif not request.form["last_name"].isalpha():
        errors.append("Name cannot contain numbers")

    if errors:
        for e in errors:
            flash(e, "error")
        return redirect("/")

    add_user_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at)\
            VALUES (:some_firstname, :some_lastname, :some_email, NOW(), NOW())"
    data = {
        "some_firstname": request.form["first_name"],
        "some_lastname": request.form["last_name"],
        "some_email": request.form["email"]
    }
    mysql.query_db(add_user_query, data)

    session["first_name"] = request.form["first_name"]
    session["Last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]

    success_query = "SELECT * FROM users"

    query_results = mysql.query_db(success_query)

    return redirect("/")



@app.route("/friends/<id>/edit", methods=["POST"])
def edit(id):

    if "id" not in session:
        return redirect("/")

    user_from_query = "SELECT * FROM friends WHERE id = :some_id"
    data = {
        "some_id": session["id"]
    }

    edit_query = ""


    staticfile = url_for("static", filename="style.css")
    return render_template("friends.html", user=user_from_query[0], messages=flash_messages)



@app.route("/friends/<id>")
def update(id):

    if "id" not in session:
        return redirect("/")

    query = "SELECT * FROM friends WHERE id = :some_id"
    data = {
        "some_id": session["id"]
    }

@app.route("/friends/<id>/delete")
def destroy(id):

    if "id" not in session:
        return redirect("/")

    query = "SELECT * FROM friends WHERE id = :some_id"
    data = {
        "some_id": session["id"]
    }

app.run(debug=True)