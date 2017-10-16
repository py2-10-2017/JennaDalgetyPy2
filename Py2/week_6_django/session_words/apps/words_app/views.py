from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):
    
    if "word" not in request.session:
        request.session["word"] = []

    if "style" not in request.session:
        request.session["style"] = []


    context = {
        "words": request.session["word"],
        "styles":request.session["style"],
        "time": datetime.datetime.now()
    }

    return render(request, "index.html", context)


def choices(request):
    request.session["word"].append(request.POST["word"])

    if request.POST.get("color_red") is not None:
        request.session["style"].append(request.POST["color_red"])
    if request.POST.get("color_green") is not None:
        request.session["style"].append(request.POST["color_green"])
    if request.POST.get("color_blue") is not None:
        request.session["style"].append(request.POST["color_blue"])

    request.session.modified = True

    return redirect("/session_words")


def clear(request):
    request.session.flush()
    return redirect("/session_words")