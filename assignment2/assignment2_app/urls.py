from django.contrib import admin
from django.urls import path, include
from assignment2_app import views
from .views import books_list_create

urlpatterns = [
    path('bookapi/',books_list_create.as_view())
]