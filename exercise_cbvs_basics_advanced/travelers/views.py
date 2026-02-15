from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from travelers.models import Traveler
from travelers.forms import TravelForm


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        messages.success(self.request, 'Traveler created successfully.')
        return super().form_valid(form)


class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('common:home')