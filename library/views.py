from django.shortcuts import render
from book.models import Book
from .serializer import bookSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# @login_required
def get_all_books(request):
    # if request.user.is_authenticated:
    try:
        all_books = Book.objects.all()
    except Book.DoesNotExist:
        return HttpResponse(status = 404)

    serializer = bookSerializer(all_books, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)