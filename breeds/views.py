from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Breed

# Create your views here.

#used a class to just render all the breeds in the db
class BreedList(generic.ListView):
    model = Breed
    template_name = "breeds/breed_list.html"
    context_object_name = 'breeds'
    paginate_by = 6


# view to access the db using the slug to get the correct db data
def breed_detail(request, slug):
    breed = get_object_or_404(Breed, slug=slug)
    return render(request, 'breeds/breed_detail.html', {'breed': breed})