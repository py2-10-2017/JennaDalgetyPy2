from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

import re
import bcrypt



# Create your views here.
def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)



def index(request):
    return render(request, "login_reg/index.html")



def register(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)

        if not errors:
            hash_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())

            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=hash_pw, birthdate = request.POST["birthdate"])

            request.session['id'] = user.id

            return redirect("/success")

        flash_errors(errors, request)

    return redirect('/')



def login(request):
    if request.method =="POST":
        check = User.objects.validate_login(request.POST)
        if "user" in check:
            request.session["id"] = check["user"].id
            return redirect("/friends")
        flash_errors(check["errors"], request)
        
    return redirect("/success")



def success(request):
    context = {
        "user": User.objects.get(id=request.session["id"]).first_name
    }
    
    return render(request, "login_reg/success.html", context)
