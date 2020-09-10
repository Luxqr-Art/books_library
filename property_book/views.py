from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *


def welcome(request):
    return render(request, 'index4.html')


def property_orm(request):
    books = Property_book.objects.all()
    books_list_str = ['<li>' + book.serial_number + ' - ' + book.title.title + '</li>' for book in books]
    # или так можно  если не использовать лист комприхеншен
    # books_list_str = ''
    # for book in books:
    #     books_list_str += '<li>' + str(book.id) + ' - ' + book.title + '</li>'
    return HttpResponse(books_list_str)


def books_json(request):
    books = Property_book.objects.all().values('title__title', 'title__author__book_author',
                                               'title__genre__book_genre', 'serial_number',
                                               'shelf', 'rack', 'property_status__title'
                                               )
    book_data = list(books)

    return JsonResponse(book_data, safe=False)

# def books_find(request):
#
#     books = Property_book.objects.filter(title_id=5).values(
#         'title__title',
#         'title__author__book_author',
#         'serial_number',
#     )
#
#
#     book_data = list(books)
#
#     return JsonResponse(book_data, safe=False)


def books_find(request):

    books = Property_book.objects.get(id=3)

    return JsonResponse(books, safe=False)