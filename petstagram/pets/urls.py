from django.urls import path, include
from pets import views

app_name = "pets"

pets_patterns = [
    path('', views.PetDetailView.as_view(), name='details'),
    path('edit/', views.PetEditView.as_view(), name='edit'),
    path('delete/', views.PetDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('add/', views.PetAddView.as_view(), name='add'),
    path('<str:username>/pet/<slug:pet_slug>/', include(pets_patterns))
]
