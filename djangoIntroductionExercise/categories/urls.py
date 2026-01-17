from django.urls import path

import categories
from categories import views

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
]