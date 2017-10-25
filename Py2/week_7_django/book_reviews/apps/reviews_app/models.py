from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []

        if len(form_data["first_name"]) < 2:
            errors.append("First Name must be valid in length")
        if not form_data["first_name"].isalpha():
            errors.append("Please enter a valid First Name")
        if len(form_data["last_name"]) < 2:
            errors.append("Last Name must be valid in length")
        if not form_data["last_name"].isalpha():
            errors.append("Please enter a valid Last Name")
        if not EMAIL_REGEX.match(form_data["email"]):
            errors.append("Please enter a valid Email")
        if len(form_data["password"]) == 0:
            errors.append("Must enter a password")
        if len(form_data["password"]) < 8:
            errors.append("Password must be at least 8 characters long")
        if form_data["password"] != form_data["confirm_pw"]:
            errors.append("Passwords do not match")

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    desc = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
