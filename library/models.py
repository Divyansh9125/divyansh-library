from django.db import models
from book.models import Book
from user.models import UserProfile

class Check_out(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)