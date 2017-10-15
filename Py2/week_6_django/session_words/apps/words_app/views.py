from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(req):
    return render(req, "index.html")


def choices(req):
    request.session["word"] = request.POST["word"]
    request.session["color_red"] = request.POST["color_red"]
    request.session["color_green"] = request.POST["color_green"]
    request.session["color_blue"] = request.POST["color_blue"]
    request.session["big_font"] = request.POST["big_font"]

    context = {
        "words": request.session["word"],
        "color_red": request.session["color_red"],
        "color_green": request.session["color_green"],
        "color_blue": request.session["color_blue"],
        "big_font": request.session["big_font"],
        "time": datetime.datetime.now()
    }

    return redirect("/session_words", context)


def clear(req):
    request.session.flush()
    return redirect("/session_words")