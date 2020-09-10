from django.db import models


class Books(models.Model):
    class Meta:
        db_table = 'books'
        verbose_name = 'book'
        verbose_name_plural = 'books'

    title = models.CharField(blank=False, null=False, max_length=20, verbose_name='title')

    author = models.ManyToManyField('BooksAuthor', blank=True)

    def authors(self):
        return ',  '.join([i.book_author for i in self.author.all()])

    genre = models.ManyToManyField('BookGenre', blank=True)

    def genres(self):
        return ', '.join([i.book_genre for i in self.genre.all()])

    def __str__(self):
        return self.title


class BookGenre(models.Model):
    class Meta:
        db_table = 'genries_book'
        verbose_name = 'genre book'
        verbose_name_plural = 'genre books'

    book_genre = models.CharField(blank=False, null=False, max_length=30, verbose_name='Genre')

    def __str__(self):
        return self.book_genre


class BooksAuthor(models.Model):
    class Meta:
        db_table = 'authors_book'
        verbose_name = 'author book'
        verbose_name_plural = 'author books'

    book_author = models.CharField(blank=False, null=False, max_length=30, verbose_name='Author',
                                   help_text='Full Name')

    def __str__(self):
        return self.book_author
