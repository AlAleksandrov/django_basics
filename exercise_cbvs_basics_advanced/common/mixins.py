from django.http import HttpResponseRedirect
from django.urls import reverse

from travelers.models import Traveler


class RecentObjectMixin:
    recent_result_limit = 3
    def get_queryset(self):
        return super().get_queryset()[:self.recent_result_limit]


class AgeRestrictionMixin:

    def dispatch(self, request, *args, **kwargs):
        traveler_id = kwargs.get('pk') or request.GET.get('user_id')
        if traveler_id:
            try:
                traveler = Traveler.objects.get(pk=traveler_id)
            except Traveler.DoesNotExist:
                return HttpResponseRedirect(reverse('common:home-teen'))

        if traveler.age < 21:
            return HttpResponseRedirect(reverse('common:home-teen'))

        return super().dispatch(request, *args, **kwargs)