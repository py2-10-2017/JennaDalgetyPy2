from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')



def process_survey(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]

    return redirect('/result')



def result(request):
    try:
        request.session["count"] += 1
    except:
        if not "count" in request.session:
            request.session["count"] = 0
    context = {
        "name": request.session["name"],
        "location": request.session["location"],
        "language": request.session["language"],
        "comment": request.session["comment"]
    }

    return render(request, "result.html", request.session["count"], request.session["name"], request.session["location"], request.session["comment"], context)