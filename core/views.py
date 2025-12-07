from django.shortcuts import render
from .models import Book, BookStatus, Author
# Create your views here

def book_list(request):

    books = Book.objects.all().prefetch_related('author')
    context = {'books':books, 'heading': 'All Books'}

    return render(request, 'core/book_list.html', context)

def reading_list(request):

    books_reading = Book.objects.filter(status=BookStatus.READING).select_related('author')
    context = {'books':books_reading, 'heading':'Currently Reading'}

    return render(request, 'core/book_list.html', context)

def completed_reading(request):

    completed_list = Book.objects.filter(status=BookStatus.COMPLETED).select_related('author')
    context = {'books':completed_list, 'heading':'Completed Reading'}

    return render(request, 'core/book_list.html', context )

def want_to_read(request):

    want_to_read_list = Book.objects.filter(status=BookStatus.WANT_TO_READ). select_related('author')
    context = {'books':want_to_read_list, 'heading':'Want to Read'}

    return render(request, 'core/book_list.html', context)

def old_books_list(request):

    old_books = Book.objects.filter(publication_year__lte=2000).select_related('author').order_by('publication_year')
    context = {'books':old_books, 'heading':"Classics (Publication Year - 2000 or Earlier)"}

    return render(request, 'core/book_list.html', context)
