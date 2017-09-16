
from flask import Flask, render_template, session, redirect

import random

app = Flask(__name__)

app.secret_key = "098hf7b5836b83724bfn3"


@app.route("/")

def index():

    return render_template("index.html")


@app.route("/guess", methods=["POST"])

def guess():

    print("in Guess function")

    past_guesses = []

    session["answer"] = 1

    guess = session["guess"]

    if session["guess"] in past_guesses:
        pass
    elif session["guess"] == session["answer"]:
        return render_template("you_win.html")
    else:
        past_guesses.append(session["guess"])
        if session["guess"] < session["answer"]:
            return render_template("too_low.html")
        elif session["guess"] > session["answer"]:
            return render_template("too_high.html")



app.run(debug=True)