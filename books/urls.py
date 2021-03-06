from django.urls import path
from .views import *


urlpatterns = [
    path('', welcome),
    path('list/', books_list),
    path('listsql/', books_sql1),
    path('listsql1/', books_sql2),
    path('listomr/', books_list),
    path('ser/', BooksList.as_view()),
    path('create', BookCreate.as_view()),
    path('author/', AuthorList.as_view()),
    path('rud/<int:pk>/', BookRUD.as_view()),
    path('ser/author/<int:author_id>/', BooksFilterAuthor.as_view()),
    path('ser/bookshot/<int:author_id>/', BooksShot.as_view()),

]