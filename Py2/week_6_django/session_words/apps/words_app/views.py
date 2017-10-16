from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):   
    if "word" not in request.session:
        request.session["word"] = []

    if "color" not in request.session:
        request.session["color"] = []

    context = {
        "words": request.session["word"],
        "time": datetime.datetime.now()
    }

    return render(request, "index.html", context)


def choices(request):
    word = request.POST["word"]
    
    if "uppercase" in request.POST:
        word = request.POST['word'].upper()

    request.session['word'].append({
        'word': word,
        'color': request.POST['color'],
    })

    request.session.modified = True

    return redirect("/session_words")


def clear(request):
    request.session.flush()
    return redirect("/session_words")