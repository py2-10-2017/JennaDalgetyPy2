from flask import Flask, render_template, redirect, flash, session, request, get_flashed_messages, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "iwaurgy34h89745849ht98ghyb"

mysql = MySQLConnector(app, "login_reg")


@app.route("/")
def index():

    success_query = "SELECT * FROM users"

    query_results = mysql.query_db(success_query)

    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("index.html", users=query_results, messages = flash_messages, styles = staticfile)



@app.route("/register", methods=["POST"])
def register():

    errors = []

    if not EMAIL_REGEX.match(request.form["email"]) or len(request.form["email"]) < 1:
        errors.append("Email is not valid")

    if len(request.form["first_name"]) < 2:
        errors.append("Must enter a first name")
    elif not request.form["first_name"].isalpha():
        errors.append("Name cannot contain numbers")
    
    if len(request.form["last_name"]) < 2:
        errors.append("Must enter a last name")
    elif not request.form["last_name"].isalpha():
        errors.append("Name cannot contain numbers")

    if len(request.form["password"]) == 0:
        errors.append("Must enter a password")
    elif len(request.form["password"]) < 8:
        errors.append("Password must be at least 8 characters long")

    if request.form["password"] != request.form["confirm_password"]:
        errors.append("Passwords do not match")

    query = "SELECT * FROM users WHERE email = :email"
    data = {
        "email": request.form["email"]
    }

    db_check = mysql.query_db(query, data)

    if db_check:
        errors.append("username already exists")
    
    if errors:
        for e in errors:
            flash(e, "error")
        return redirect("/")

    hashed_pw = bcrypt.generate_password_hash(request.form["password"])

    add_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)\
            VALUES (:some_firstname, :some_lastname, :some_email, :some_password, NOW(), NOW())"
    data = {
        "some_firstname": request.form["first_name"],
        "some_lastname": request.form["last_name"],
        "some_email": request.form["email"],
        "some_password": hashed_pw
    }
    mysql.query_db(add_user_query, data)

    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]

    success_query = "SELECT * FROM users"

    query_results = mysql.query_db(success_query)

    flash("succesfully registered", "success")
    return redirect("/")



@app.route("/login", methods=["POST"])
def login():

    errors = []

    query = "SELECT password, id FROM users WHERE email = :some_email"
    data = {
        "some_email": request.form["email"]
    }
   
    friend = mysql.query_db(query, data)

    if not friend: 
        errors.append("invalid username/password")
    else:
        if not bcrypt.check_password_hash(friend[0]["password"], request.form["password"]):
            errors.append("invalid username/password")

    if errors:
        for e in errors:
            flash(e, "error")
        return redirect("/")

    session["id"] = friend[0]["id"]

    flash("succesfully logged in", "success")
    return redirect("/success")



@app.route("/success")
def success(id):

    # if "id" not in session:
    #     return redirect("/")

    query = "SELECT first_name FROM users WHERE id = friend[id]"
    data = {
        "first_name": session["first_name"]
    }

    user_from_query = mysql.query_db(query, data)

    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("success.html", user=user_from_query[0], messages=flash_messages, styles=staticfile)




app.run(debug=True)