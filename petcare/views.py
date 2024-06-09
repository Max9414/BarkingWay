from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.db.models import Q
from .models import PetCare

# Create your views here.

class PetCareList(generic.ListView):
    model = PetCare
    template_name = "petcare/petcare_list.html"
    context_object_name = 'petcares'
    paginate_by = 6


    def get_queryset(self):
        """
        allow the frontend to search
        in the database searching by
        title, description and excerpt
        """
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        title_filter = self.request.GET.get('title')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(excerpt__icontains=query)
            )

        if title_filter:
            queryset = queryset.filter(
                title__icontains=title_filter)

        return queryset


def petcare_detail(request, slug):
    petcare = get_object_or_404(PetCare, slug=slug)
    return render(request, 'petcare/petcare_detail.html', {
        'petcare': petcare})