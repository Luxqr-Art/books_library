from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome),
    path('ormjson/', reader_json),

]