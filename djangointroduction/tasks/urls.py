from django.urls import path

from tasks.views import index

urlpatterns = [
    path('', index),
]