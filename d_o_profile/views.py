from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Dog, Owner
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

#creates the view for the human profile with all the owned dogs listed and their linked profiles
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


#creates the view to see the detail of dogs linked to the current user
def dog_profile_view(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, "d_o_profile/dogprofile.html", {"dog": dog})


#creates the view for the dog profile creation
@login_required
def create_dog(request):
    form = DogForm()
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user
            dog.save()
            return redirect('human_profile') #redirects to the human profile page
    else:
        form = DogForm()
    return render(request, 'd_o_profile/dog_profile_creation.html', {'form': form})

@login_required
def modify_owner(request, owner_id):
    owner_instance = get_object_or_404(Owner, id=owner_id)
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner_instance)
        if form.is_valid():
            owner = form.save()
            return redirect('human_profile')
    else:
        form = OwnerForm(instance=owner_instance)
    return render(request, 'd_o_profile/modify_human.html', {'form': form})
