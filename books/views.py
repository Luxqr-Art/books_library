
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from books.models import *
from rest_framework import generics, filters
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MyCustomFilter


class BooksList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, MyCustomFilter]
    search_fields = ['title']
    ordering_filter = ['title']
    filterset_fields = ['author', 'genre']


class AuthorList(generics.ListAPIView):
    queryset = BooksAuthor.objects.all()
    serializer_class = AuthorSerialize


class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer


#retrive /update / delete
class BookRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BooksFilterAuthor(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Books.objects.filter(author=self.kwargs['author_id'])



class BooksShot(generics.ListAPIView):
    serializer_class = BookListSerializer

    def get_queryset(self):
        return Books.objects.filter(author=self.kwargs['author_id'])









def welcome(request):
    return render(request, 'index1.html')

def books_list(request):
    books = Books.objects.all()
    books_list_str = ['<li>' + book.title + '</li>' for book in books]
    # или так можно  если не использовать лист комприхеншен
    # for book in books:
    #     books_list_str += '<li>' + book.title + '</li>'
    return HttpResponse(books_list_str)


# ----------------------------------------------------

# сухой запрос  на прямую к sql
def books_sql1(request):
    books = Books.objects.raw('SELECT id, title FROM books')
    # books_list_str = ['<li>' + book.title + '</li>' for book in books]
    # или так можно  если не использовать лист комприхеншен
    books_list_str = ''
    for book in books:
        books_list_str += '<li>' + book.title + '</li>'
    return HttpResponse(books_list_str)


# ---------------------------------------------------

def books_sql2(request):
    # так не работает не известно почему
    # books = Books.objects.raw('SELECT property_books.id, books.title FROM \
    #                            property_books join books on books.id = property_books.title_id')
    books = Books.objects.raw('SELECT books.id, property_books.serial_number \
                               FROM books join property_books on property_books.id = books.id')
    books_list_str = ['<li>' + str(book.serial_number) + ' - ' + book.title + '</li>' for book in books]
    # или так можно  если не использовать лист комприхеншен
    # books_list_str = ''
    # for book in books:
    #     books_list_str += '<li>' + str(book.serial_number) + ' - ' + book.title + '</li>'
    return HttpResponse(books_list_str)








