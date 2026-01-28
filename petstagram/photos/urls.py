from django.urls import path, include

from photos import views

app_name = "photos"

photo_patterns = [
    path('', views.photo_details, name='details'),
    path('edit/', views.photo_edit, name='edit'),
]

urlpatterns = [
    path('add/', views.photo_add, name='add'),
    path('<int:pk>/', include(photo_patterns)),
]
