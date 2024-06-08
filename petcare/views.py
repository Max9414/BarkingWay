from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import PetCare

# Create your views here.

class PetCareList(generic.ListView):
    model = PetCare
    template_name = "petcare/petcare_list.html"
    context_object_name = 'petcares'
    paginate_by = 6


def petcare_detail(request, slug):
    petcare = get_object_or_404(PetCare, slug=slug)
    return render(request, 'petcare/petcare_detail.html', {'petcare': petcare})