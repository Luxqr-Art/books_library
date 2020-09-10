from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from books.models import Books


class Property_book(models.Model):
    class Meta:
        db_table = 'property_books'
        verbose_name = 'property Book'
        verbose_name_plural = 'property Books'

    title = models.ForeignKey(Books,
                              blank=False, null=True, verbose_name='book',
                              on_delete=models.CASCADE)

    property_Publishing_house = models.ForeignKey('Property_Publishing_house',
                                                  blank=False, null=False, verbose_name='Publisher',
                                                  on_delete=models.CASCADE)

    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1700), MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>")

    serial_number = models.CharField(blank=False, null=False, max_length=20, verbose_name='S/N')

    rack = models.CharField(blank=False, null=False, max_length=10, verbose_name='rack №')

    shelf = models.BigIntegerField(blank=False, null=False, verbose_name='shelf №')

    property_status = models.ForeignKey('Property_Status',
                                        blank=False, null=False, verbose_name='status',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Property_Publishing_house(models.Model):
    class Meta:
        db_table = 'publishing_house'
        verbose_name = 'publisher'
        verbose_name_plural = 'publishing house'

    title = models.CharField(blank=False, null=False, max_length=30, verbose_name='Publishing_house')

    def __str__(self):
        return self.title


class Property_Status(models.Model):
    class Meta:
        db_table = 'property_status'
        verbose_name = 'status'
        verbose_name_plural = 'property Status'

    Book_Choices = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable')
    )

    title = models.CharField(blank=False, null=False, max_length=20, choices=Book_Choices)

    def __str__(self):
        return self.title
