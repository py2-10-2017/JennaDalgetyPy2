from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context = {
        "word": get_random_string(length=14)
    } 
    return render(request, 'index.html', context)

def generate_word(request):
    return redirect("/")