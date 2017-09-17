from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = "9378eyf5vyrnc8n4nb3"


@app.route("/")

def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])

def process():

    if len(request.form["name"]) < 1:
        flash("Name cannot be empty")
    else:
        flash("Congratulations!  Your name is {}".format(request.form["name"]))

    return redirect("/")


app.run(debug=True)