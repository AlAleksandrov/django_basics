from django.urls import path, include

from books.views import landing_page, book_list, book_details

app_name = 'books'

books_patterns = [
    path('', book_list, name='list'),
    path('<slug:slug>/', book_details, name='details'),
]
urlpatterns = [
    path('', landing_page, name='Home'),
    path('books/', include(books_patterns)),
]