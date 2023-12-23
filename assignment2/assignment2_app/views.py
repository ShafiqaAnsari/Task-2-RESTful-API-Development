from django.shortcuts import render
from .models import books
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView

#this will list all the books and we can also add one
class books_list_create(ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = BookSerializer
