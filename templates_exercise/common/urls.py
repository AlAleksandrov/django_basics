from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('current-time/', views.current_time_view, name='current_time'),
]
