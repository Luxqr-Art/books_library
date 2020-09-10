from django.db import models
from readers.models import ReaderTicket
from property_book.models import Property_book


class Journal(models.Model):
    class Meta:
        db_table = 'journals'
        verbose_name = 'journal'
        verbose_name_plural ='journal'

    ticket = models.ForeignKey(ReaderTicket, blank=False, null=False,
                               verbose_name='library_card', on_delete=models.CASCADE)

    employee = models.ForeignKey('JournalEmployee', blank=False, null=False,
                                 verbose_name='employee', on_delete=models.CASCADE)

    book_property = models.ForeignKey(Property_book, blank=False, null=False,
                                      verbose_name='Property_book', on_delete=models.CASCADE)

    check_int = models.DateField(blank=False, null=False, verbose_name='check_int')

    check_out = models.DateField(blank=True, null=True, verbose_name='check_out')

    def __str__(self):
        return f'{self.check_int}{self.check_out}'



class JournalEmployee(models.Model):
    class Meta:
        db_table = 'employees'
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    first_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='Last name')

    def __str__(self):
        return f'{self.first_name}{self.last_name}'




