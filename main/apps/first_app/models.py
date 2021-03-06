from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    name = models.CharField(max_length= 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(User, related_name = 'uploaded_books')
    liked_users = models.ManyToManyField(User, related_name = 'liked_books')
# related name creates a variable in user called liked_books - the string entry shown above
# related name also creates a foreign key table called liked_books - string shown above