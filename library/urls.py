from django.urls import path
from . import views

urlpatterns = [
    path('books', views.get_all_books, name='All_Books'),
]