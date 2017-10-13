from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
    HttpResponse("I AM A JEDI!!!")