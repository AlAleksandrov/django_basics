from django.urls import path, include
from reviews.views import recent_reviews, review_details, review_edit, review_delete, review_create, review_bulk_edit

app_name = 'reviews'

reviews_patterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', include([
        path('', review_details, name='details'),
        path('create/', review_create, name='create'),
        path('edit/', review_edit, name='edit'),
        path('delete/', review_delete, name='delete'),

    ])),
    path('<slug:book_slug>/', review_bulk_edit, name='bulk_edit'),
]
urlpatterns = [
    path('', include(reviews_patterns)),

]