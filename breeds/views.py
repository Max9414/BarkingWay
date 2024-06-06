from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Breed

# Create your views here.

class BreedList(generic.ListView):
    model = Breed
    template_name = "breeds/breed_list.html"
    context_object_name = 'breeds'
    paginate_by = 6


def breed_detail(request, slug):
    breed = get_object_or_404(Breed, slug=slug)
    return render(request, 'breeds/breed_detail.html', {'breed': breed})