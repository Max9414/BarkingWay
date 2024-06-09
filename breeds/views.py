from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.db.models import Q
from .models import Breed

# Create your views here.

#used a class to just render all the breeds in the db
class BreedList(generic.ListView):
    model = Breed
    template_name = "breeds/breed_list.html"
    context_object_name = 'breeds'
    paginate_by = 6


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        breed_filter = self.request.GET.get('breed')

        if query:
            queryset = queryset.filter(
                Q(breed__icontains=query) |
                Q(description__icontains=query) |
                Q(excerpt__icontains=query)
            )

        if breed_filter:
            queryset = queryset.filter(
                breed__icontains=breed_filter)

        return queryset


def breed_detail(request, slug):
    breed = get_object_or_404(Breed, slug=slug)
    return render(request, 'breeds/breed_detail.html', {'breed': breed})