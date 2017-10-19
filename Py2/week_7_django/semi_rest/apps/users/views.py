from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        "all_users": users
    }
    return render(request, "index.html", context)

def create(request):
    User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
    return redirect("/users")


def new(request):
    return render(request, "add_user.html")


def show(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "show.html", context)


def edit(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "edit.html", context)


def update(request, id):
    user_update = User.objects.get(id=id)
    user_update.first_name = request.POST["first_name"]
    user_update.last_name = request.POST["last_name"]
    user_update.email = request.POST["email"]
    user_update.save()
    return redirect("/users/<id>")


def destroy(request, id):
    user_destroy = User.objects.get(id=id)
    user_destroy.delete()

    return redirect("/users")


