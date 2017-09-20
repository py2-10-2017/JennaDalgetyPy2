from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = "iuvbierwvbewurvybch 9u8yu3hui"


@app.route("/")

def index():

    return render_template("index.html")



@app.route("/user", methods=['POST'])

def create_user():

    errors = False

    if len(request.form["name"]) < 1:
        flash("Name cannot be blank")
        errors = True
    else:
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
    if len(request.form["comment"]) > 120:
        flash("Comment cannot be longer than 120 characters")
        errors = True
    elif len(request.form["comment"]) < 1:
        flash("Comment cannot be blank")
        errors = True
    else:
        session["comment"] = request.form["comment"]

    if errors:
        return redirect("/")
    else:
        return redirect("/results")



@app.route("/results")

def return_results():

    return render_template("results.html")




app.run(debug=True)