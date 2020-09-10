from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse, JsonResponse


def welcome(request):
    return render(request, 'index3.html')

def reader_json(request):
    books = Reader.objects.all().values(
        'first_name',
        'last_name',
        'birthday',
        'readeraddress__city_reader',
        'readeraddress__street_reader',
        'readeraddress__house_reader',
        'readerphone__phone_number',
        'readerticket__ticket_number',
        'readerticket__journal__book_property',
        'readerticket__journal__employee_id'


    )
    book_data = list(books)

    return JsonResponse(book_data, safe=False)
