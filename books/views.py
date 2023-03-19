from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import BooksModel, AuthorModel, PublisherModel
from .forms import BookForm

# Create your views here.

def books(request):
    allBooks = BooksModel.objects.all()
    return render(request, 'books/books.html', {'books':allBooks})


def book(request, pk):
    book = BooksModel.objects.get(id=pk)
    return render(request, 'books/single-book.html', {'book': book})


def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')

    
    context = {'form':form}
    return render(request,'books/book-form.html', context)


def editBook(request, pk):
    book = BooksModel.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')

    
    context = {'form':form}
    return render(request,'books/book-form.html', context)


def authors(request):
    allAuthors = AuthorModel.objects.all()
    return render(request, 'books/authors.html', {'authors':allAuthors})


def publishers(request):
    allPublishers = PublisherModel.objects.all()
    return render(request, 'books/publishers.html', {'publishers':allPublishers})


