from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AddForm


def index(request):
    return render(request,'index.html')


def add(request):
    error=''
    if request.method =='POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
        else:
            error = 'Форма была неверной'

    
    form = AddForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request,'add.html', context)


def authors(request):
    authors = Author.objects.all()
    return render(request,'authors.html', {"authors" : authors})

def books(request):
    books = Book.objects.all()
    return render(request,'books.html', {"books" : books})