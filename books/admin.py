from django.contrib import admin
from books.models import Books, BooksAuthor, BookGenre

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'authors', 'genres', 'owner']

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['book_genre']

@admin.register(BooksAuthor)
class BooksAuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_author']


# это делает наш декоратор когда мы его на вешиваем
# admin.site.register(BooksAuthor, BooksAuthorAdmin)
