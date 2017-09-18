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

    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email Address!")






app.run(debug=True)