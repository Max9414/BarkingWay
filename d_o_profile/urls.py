from django.urls import path
from d_o_profile.views import human_profile_view, dog_profile_view

urlpatterns = [
    path('profile/', human_profile_view, name="human_profile"),
    path('dog/<int:dog_id>', dog_profile_view, name="dog_profile"),
]