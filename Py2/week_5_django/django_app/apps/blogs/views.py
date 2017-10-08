from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)


def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)


def create(request):
    return redirect("/")

def show(request):
    response = "placeholder to display blog {{number}}"
    return HttpResponse(response)


# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
def edit(request):
    response = "placeholder to edit blog {{number}}"
    return HttpResponse(response)



# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /. 
def delete(request):
    return redirect("/")