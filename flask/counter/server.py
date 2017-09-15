from flask import Flask, session, render_template, redirect

app = Flask(__name__)

app.secret_key = "92qf8ybntybn49iunvu"


@app.route("/")

def index():

    session["count"] = 0

    return render_template("index.html")

   



@app.route("/add")

def add_to_count():

    session["count"] += 1

    return redirect("/")


app.run(debug=True)