# Generated by Django 3.1 on 2020-09-04 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booksauthor',
            options={'verbose_name': 'author book', 'verbose_name_plural': 'author books'},
        ),
        migrations.AlterModelTable(
            name='bookgenre',
            table='genries_book',
        ),
        migrations.AlterModelTable(
            name='books',
            table='books',
        ),
        migrations.AlterModelTable(
            name='booksauthor',
            table='authors_book',
        ),
    ]
