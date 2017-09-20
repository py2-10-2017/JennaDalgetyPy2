from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "iuvbierwvbewurvybch 9u8yu3hui"


@app.route("/")

def index():

  return render_template("index.html")



@app.route("/user", methods=['POST'])

def create_user():

  session["name"] = request.form["name"]
  session["location"] = request.form["location"]
  session["language"] = request.form["language"]
  session["comment"] = request.form["comment"]

  return redirect("/results")



@app.route("/results")

def return_results():

  return render_template("results.html")




app.run(debug=True)