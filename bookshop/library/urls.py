from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('authors', views.authors, name='authors'),
    path('books', views.books, name='books'),
]
