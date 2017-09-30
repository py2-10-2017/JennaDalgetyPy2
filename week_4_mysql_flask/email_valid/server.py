from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, url_for, session
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "iwb38y4938vy3u4ir"
mysql = MySQLConnector(app, "email_valid")



@app.route("/")
def index():
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("index.html", messages = flash_messages, styles = staticfile)



@app.route("/register", methods=["POST"])
def register():
    errors = []

    if not EMAIL_REGEX.match(request.form["email"]):
        errors.append("Email is not valid!")
    if len(request.form["email"]) < 1:
        errors.append("Email is not valid!")

    query = "SELECT * FROM users WHERE email = :some_email"
    data = {
        "some_email": request.form["email"]
    }

    if mysql.query_db(query, data):
        errors.append("email already exists")

    if errors:
        for e in errors:
            flash(e, "error")
        return redirect("/")

    query = "INSERT INTO users (email, created_at, updated_at)\
            VALUES (:some_email, NOW(), NOW())"
    data = {
        "some_email": request.form["email"],
    }

    mysql.query_db(query, data)

    session["email"] = request.form["email"]

    flash("succesfully registered", "success")
    return redirect("/success")



@app.route("/success")
def success():

    success_query = "SELECT * FROM users"

    query_results = mysql.query_db(success_query)

    flash_messages = get_flashed_messages(with_categories=True)

    flash("The email address you entered ({}) is a VALID email address!  Thank you!".format(session["email"]), "success")

    staticfile = url_for("static", filename="style.css")
    return render_template("success.html", users=query_results, messages=flash_messages)



app.run(debug=True)