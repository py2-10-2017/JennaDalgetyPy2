from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, url_for, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "iwb38y4938vy3u4ir"
mysql = MySQLConnector(app, "demo_reg")

@app.route("/")
def index():
    flash messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("index.html", messages = flash_messages, styles = staticfile)

@app.route("/register", methods=["POST"])
def register():
    errors = []

    # min length of username
    if len(request.form["username"]) < 5:
        errors.append("username must be 5 or more characters long")

    # min length of password
    if len(request.form["password"]) < 8:
        errors.append("password must be 8 or more characters long")

    # password matches
    if request.form["password"] != request.form["confirm_password"]:
        errors.append("passwords do not match")

    # username must be unique
    query = "SELECT * FROM friends WHERE username = :some_username"
    data = {
        "some_username": request.form["username"]
    }

    # if this is a non-empty list, we have someone with that username
    if mysql.query_db(query, data)
        errors.append("username already exists")

    # check errors list, then redirect
    if errors:
        # flash each error in list, then redirect
        for e in errors:
            flash(e, "error")
        return redirect("/")

    hashed_pw = bcrypt.generate_password_hash(request.form["password"])

    # create a friend row in db
    query = "INSERT INTO friends (username, password)\
            VALUES (:some_username, :some_password)"
    data = {
        "some_username": request.form["username"],
        "some_password": hashed_pw
    }
    mysql.query_db(query, data)

    flash("succesfully registered", "success")
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():

    errors = []

    # does username exist
    query = "SELECT password, id FROM friends WHERE username = :some_username"
    data = {
        "some_username": request.form["username"]
    }
    # if this is an empty list, we don't have someone with that username
    friend = mysql.query_db(query, data)
    if not friend: 
        errors.append("invalid username/password")
    else:
        # if it does, does the password match (using bcrypt to compare hashes)
        if not bcrypt.check_password_hash(friend[0]["password"], request.form["password"]):
            errors.append("invalid username/password")

    if errors:
        # flash each error in list, then redirect
        for e in errors:
            flash(e, "error")
        return redirect("/")

    # store user's id to session
    session["id"] = friend[0]["id"]

    flash("succesfully logged in", "success")
    return redirect("/success")

#login restricted
@app.route("/success")
def success():
    # check sesson for "id" before we do anything
    if "id" not in session:
        return redirect("/")
    # access user from session id using a db query
    query = "SELECT * FROM friends WHERE id = :some_id"
    data = {
        "some_id": session["id"]
    }
    flash messages = get_flashed_messages(with_categories=True)
    staticfile = url_for("static", filename="style.css")
    return render_template("success.html", user=user_from_query[0], messages=flash_messages, styles=staticfile)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/post_message", methods=["POST"])
def post_message():

    query = "INSERT INTO messages (content, friend_id)\
        VALUES(:some_message, :some_friend)"
    data = {
        ":some_message": request.form["content"],
        ":some_friend": session["id"]
    }
    mysql.query_db(query, data)
    return redirect("/success")


app.run(debug=True)