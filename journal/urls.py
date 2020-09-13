from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome),
    path('ormjson/', journal_json),
    path('list/', JournalList.as_view()),
]