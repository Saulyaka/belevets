from django.utils import timezone
from django.views import generic

from .models import PleinAir


class PleinairView(generic.ListView):
    model = PleinAir
    template_name = 'pleinair/pleinairs.html'
    context_object_name = 'pleinairs'

    def get_queryset(self):
        pleinairs = super().get_queryset()
        pleinair_future = []
        for pleinair in pleinairs:
            if pleinair.start > timezone.now():
                pleinair_future.append(pleinair)
        return pleinair_future


class DetailView(generic.DetailView):
    model = PleinAir
    template_name = 'pleinair/details.html'
    context_object_name = 'pleinair'
