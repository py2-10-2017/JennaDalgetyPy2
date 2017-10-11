from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def buy(request):
    request.session[""]

    return redirect("/checkout")

def checkout(request):
    return render(request, "checkout.html")