from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name = 'book_list'),
    path('reading/', views.reading_list, name = 'reading_list'),
    path('completed/', views.completed_reading, name = 'completed_list'),
    path('want_to_read/', views.want_to_read, name = 'want_to_read_list'),
    path('old_books_list/', views.old_books_list, name = 'old_books_list'),
   
    
]
