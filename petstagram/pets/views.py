from django.db.models import Prefetch
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from common.mixin import CheckUserIsOwner
from pets.forms import PetForm
from pets.models import Pet
from photos.models import Photo


# Create your views here.

class PetAddView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse('accounts:details', kwargs={'pk':self.object.user.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class PetDetailView(DetailView):
    queryset = Pet.objects.prefetch_related(
        Prefetch(
            'photo_set',
            queryset=Photo.objects.prefetch_related('tagged_pets', 'like_set'),
        )
    )
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-details-page.html'


class PetEditView(CheckUserIsOwner, UpdateView):
    model = Pet
    form_class = PetForm
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-edit-page.html'

    def get_success_url(self) -> str:
        return reverse(
            'pets:details',
            kwargs={
                'username': 'username',
                'pet_slug': self.object.slug
            }
        )


class PetDeleteView(CheckUserIsOwner, DeleteView):
    model = Pet
    form_class = PetForm
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-delete-page.html'

    def get_success_url(self):
        return reverse('accounts:details', kwargs={'pk':self.object.user.pk})

    def get_initial(self) -> dict:
        return self.object.__dict__

