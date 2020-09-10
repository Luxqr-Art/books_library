from django.urls import path
from .views import *


urlpatterns = [
    path('', welcome),
    path('ormfind/', books_find),
    path('ormhttp/', property_orm),
    path('ormjson/', books_json),
]