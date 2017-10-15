from django.shortcuts import render, redirect, HttpResponse
import datetime
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    return render(request, "index.html")


def choices(request):
    try:
        request.session["word"] = request.POST["word"]
    except MultiValueDictKeyError: 
        request.session["word"] = False
    try:
        request.session["color_red"] = request.POST["color_red"]
    except MultiValueDictKeyError:
        request.session["color_red"] = False
    try:    
        request.session["color_green"] = request.POST["color_green"]
    except MultiValueDictKeyError:
        request.session["color_green"] = False
    try:    
        request.session["color_blue"] = request.POST["color_blue"]
    except MultiValueDictKeyError:
        request.session["color_blue"] = False
    try:    
        request.session["big_font"] = request.POST["big_font"]
    except MultiValueDictKeyError:    
        request.session["big_font"] = False

    context = {
        "words": request.session["word"],
        "color_red": request.session["color_red"],
        "color_green": request.session["color_green"],
        "color_blue": request.session["color_blue"],
        "big_font": request.session["big_font"],
        "time": datetime.datetime.now()
    }

    return redirect("/session_words", context)


def clear(request):
    request.session.flush()
    return redirect("/session_words")