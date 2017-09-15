from flask import Flask, session, render_template, redirect

app = Flask(__name__)

app.secret_key = "92qf8ybntybn49iunvu"


@app.route("/")

def index():

    if not "count" in session:
        session["count"] = 0


    return render_template("index.html")

   



@app.route("/add")

def add_to_count():

    session["count"] += 1

    print session["count"]

    return redirect("/")


app.run(debug=True)