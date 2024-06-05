from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Dog, Owner
from django.contrib.auth.models import User

# Create your views here.

def human_profile_view(request):
    if request.user.is_authenticated:
        try:
            owner = Owner.objects.get(name=request.user)
            owned_dogs = Dog.objects.filter(owner=request.user)
            return render(request, "d_o_profile/humanprofile.html", {"owner": owner, "owned_dogs": owned_dogs})
        except Owner.DoesNotExist:
            return HttpResponse("No owner found for the logged in user")
    else:
        return HttpResponse("User is not authenticated.")


def dog_profile_view(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, "d_o_profile/dogprofile.html", {"dog": dog})
