from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics
from .serializers import *

class JournalList(generics.ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer










def welcome(request):
    return render(request, 'index2.html')


def journal_json(request):
    books = Journal.objects.all().values(
        'ticket__reader__last_name',
        'ticket__reader__first_name',
        'ticket__reader__birthday',
        'book_property__title__title',
        'ticket__ticket_number',
        'book_property__title__author',
    )

    book_data = list(books)

    return JsonResponse(book_data, safe=False)
