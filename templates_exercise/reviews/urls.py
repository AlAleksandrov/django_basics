from django.urls import path, include

from reviews.views import recent_reviews, review_details, review_edit, review_delete

app_name = 'reviews'

reviews_patterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_details, name='details'),
    path('<int:pk>/edit/', review_edit, name='edit'),
    path('<int:pk>/delete/', review_delete, name='delete'),
]
urlpatterns = [
    path('', include(reviews_patterns)),

]