from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome),
    path('ormjson/', journal_json),
    # path('listsql/', books_sql1),
]