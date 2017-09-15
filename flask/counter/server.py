from flask import Flask, session, render_template

app = Flask(__name__)

app.secret_key = "92qf8ybntybn49iunvu"


@app.route("/")

def index():

    counter = 1

    return render_template("index.html")

   
    counter += 1

    session["counter"] = counter



app.run(debug=True)