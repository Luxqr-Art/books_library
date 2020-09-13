from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerialize(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'title',
            'author'
        ]