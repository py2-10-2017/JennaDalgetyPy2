
from flask import Flask, render_template, session, redirect, request

import random

app = Flask(__name__)

app.secret_key = "098hf7b5836b83724bfn3"


@app.route("/", methods=["POST", "GET"])

def index():

    if not "answer" in session:
        session["answer"] = random.randint(1, 100)


    return render_template("index.html")


@app.route("/guess", methods=["POST"])

def guess():


    session["guess"] = int(request.form["guess"])
    
    print "guess:", session["guess"], "answer:", session["answer"]

    if session["guess"] == session["answer"]:
        return render_template("you_win.html")
    else:
        if session["guess"] < session["answer"]:
            return render_template("too_low.html")
        elif session["guess"] > session["answer"]:

            return render_template("too_high.html")


@app.route("/reset", methods=["POST"])

def reset():

    session["answer"] = random.randint(1, 100)

    return redirect("/")



app.run(debug=True)