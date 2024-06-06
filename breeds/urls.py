from django.urls import path
from .views import BreedList, breed_detail

urlpatterns = [
    path('', BreedList.as_view(), name="breed_list"),
    path('details/<slug:slug>', breed_detail, name='breed_detail')
]