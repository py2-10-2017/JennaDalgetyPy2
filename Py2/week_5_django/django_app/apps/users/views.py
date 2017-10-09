from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def new_user(request):
    return redirect("/register")

def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)