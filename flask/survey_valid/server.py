from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = "iuvbierwvbewurvybch 9u8yu3hui"


@app.route("/")

def index():

    if not "errors" in session:
        session["errors"] = []

    return render_template("index.html")



@app.route("/user", methods=['POST'])

def create_user():

    if len(request.form["name"]) < 1:
        session["errors"].append(flash("Name cannot be blank"))
        print("appending 1")
        return redirect("/")
    else:
        session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    if len(request.form["comment"]) > 120:
        session["errors"].append(flash("Comment cannot be longer than 120 characters"))
        return redirect("/")
    elif len(request.form["comment"]) < 1:
        session["errors"].append(flash("Comment cannot be blank"))
    else:
        session["comment"] = request.form["comment"]

    return redirect("/results")



@app.route("/results")

def return_results():

    return render_template("results.html")




app.run(debug=True)