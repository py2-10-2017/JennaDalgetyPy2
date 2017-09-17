from flask import Flask, render_template, session, redirect, request

import random, datetime

app = Flask(__name__)

app.secret_key = "owifuhb3n49hf5849p4jn38"


@app.route("/", methods=["GET", "POST"])

def index():

    if not "gold" in session:
        session["gold"] = 0
    if not "activities" in session:
        session["activities"] = []
    return render_template("index.html")



@app.route("/process_money", methods=["GET", "POST"])

def process_money():

    
    earned = 0
    print("In process_money function")

    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))    

        if value == "farm":
            earned = random.randint(10, 20)
            message = 'Earned '+str(earned)+' gold from the farm! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        elif value == "cave":
            earned = random.randint(5, 10)
            message = 'Earned '+str(earned)+' gold from the cave! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        elif value == "house":
            earned = random.randint(2, 5)
            message = 'Earned '+str(earned)+' gold from the house! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        elif value == "casino":
            earned = random.randint(-50, 50)
            message = 'Entered a casino and won '+str(earned)+' gold! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            if earned < 0:
                message = 'Entered a casino and lost '+str(earned)+' gold.  Ouch. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            elif earned == 0:
                message = 'Entered a casino and broke even. {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    session["gold"] += earned
    session["activities"].insert(0, message)


    return redirect('/')




app.run(debug=True)