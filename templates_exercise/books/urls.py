from django.urls import path, include

from books.views import landing_page, book_list, book_details, book_create, book_edit, book_delete
from reviews.views import review_create

app_name = 'books'

books_patterns = [
    path('', book_list, name='list'),
    path('create/', book_create, name='create'),
    path('<int:pk>/', include ([
        path('edit/', book_edit, name='edit'),
        path('delete/', book_delete, name='delete'),
        path('review/create/', review_create, name='review_create'),
    ])),
    path('<slug:slug>/', book_details, name='details'),
]
urlpatterns = [
    path('', landing_page, name='Home'),
    path('books/', include(books_patterns)),
]