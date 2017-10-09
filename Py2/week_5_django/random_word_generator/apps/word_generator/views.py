from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try:
        request.session["count"] += 1
    except:
        if not "count" in request.session:
           request.session["count"] = 0

    context = {
        "word": get_random_string(length=14)
    } 
    return render(request, 'index.html', context, request.session.count)

def generate_word(request):
    return redirect("/")