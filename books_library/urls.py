
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('books/', include('books.urls')),
    path('book/', include('property_book.urls')),
    path('journal/', include('journal.urls')),
    path('reader/', include('readers.urls'))
]
