from django.urls import path
from .views import *


urlpatterns = [
    path('', welcome),
    path('list/', books_list),
    path('listsql/', books_sql1),
    path('listsql1/', books_sql2),
    path('listomr/', books_list),
    path('ser/', BooksList.as_view()),
    path('rud/<int:pk>/', BookRUD.as_view()),

]