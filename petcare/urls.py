from django.urls import path
from .views import PetCareList, petcare_detail

urlpatterns = [
    path('', PetCareList.as_view(), name="petcare_list"),
    path('details/<slug:slug>', petcare_detail, name='petcare_detail')
]