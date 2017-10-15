from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):
    
    if "word" not in request.session:
        request.session["word"] = []


    context = {
        "words": request.session["word"],
        "time": datetime.datetime.now()
    }

    return render(request, "index.html", context)


def choices(request):
    request.session["word"].append(request.POST["word"])

    styles = {
        
    }



    request.session.modified = True

    return redirect("/session_words")


def clear(request):
    request.session.flush()
    return redirect("/session_words")