from django.urls import path
from d_o_profile.views import *

urlpatterns = [
    path('profile/', human_profile_view, name="human_profile"),
    path('dog/<int:dog_id>', dog_profile_view, name="dog_profile"),
    path('create-dog/', create_dog, name="dog_creation"),
]