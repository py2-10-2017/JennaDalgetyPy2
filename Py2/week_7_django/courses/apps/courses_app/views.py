from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        "all_courses": courses
    }
    return render(request, "courses_app/index.html", context)


def create(request):
    if len(request.POST["course_name"]) < 5:
        messages.error(request, "Course Name must be 5 characters or more in length")
    if len(request.POST["desc"]) < 15:
        messages.error(request, "Course Description must be 15 characters or more in length")
        return redirect("/")
    else:
        Course.objects.create(course_name=request.POST["course_name"], desc=request.POST["desc"])
    return redirect("/")


def confirm_delete(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "courses_app/destroy.html", context)


def destroy(request, id):
    course_destroy = Course.objects.get(id=id)
    course_destroy.delete()
    return redirect("/")