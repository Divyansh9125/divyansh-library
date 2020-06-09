from django.db import models

class Book(models.Model):

    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=2500)
    author = models.CharField(max_length=2500)
    year = models.DateField(auto_now=False, auto_now_add=False)
    publisher = models.CharField(max_length=300)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


