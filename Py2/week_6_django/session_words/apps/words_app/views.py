from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")


def choices(request):
    if request.POST.get("word"):
        request.session["word"] = request.POST.get("word")
    if request.POST.get("color_red"):
        request.session["color_red"] = request.POST.get("color_red")  
    if request.POST.get("color_green"):
        request.session["color_green"] = request.POST.get("color_green")
    if request.POST.get("color_blue"):
        request.session["color_blue"] = request.POST.get("color_blue") 
    if request.POST.get("big_font"):
        request.session["big_font"] = request.POST.get("big_font")

    context = {
        "words": request.session["word"],
        "color_red": request.session["color_red"],
        "color_green": request.session["color_green"],
        "color_blue": request.session["color_blue"],
        "big_font": request.session["big_font"],
        "time": datetime.datetime.now()
    }

    print("through context")

    return redirect("/session_words", context)


def clear(request):
    request.session.flush()
    return redirect("/session_words")