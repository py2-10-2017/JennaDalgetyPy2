from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')



def process_survey(request):
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]

    return redirect('/results')



def result(request):
    try:
        request.session["count"] += 1
    except:
        if not "count" in request.session:
            request.session["count"] = 0
    context = {
        "name": session["name"],
        "location": session["location"],
        "language": session["language"],
        "comment": session["comment"]
    }

    return render(request, "result.html", request.session["count"], context)