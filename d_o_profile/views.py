from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from allauth.account.views import SignupView
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Dog, Owner
from django.contrib.auth.models import User
from events.models import Event
from .forms import *

# Create your views here.


#creates the view for the human profile with all the owned dogs listed and their linked profiles
def human_profile_view(request):
    if request.user.is_authenticated:
        try:
            owner = Owner.objects.get(name=request.user)
            owned_dogs = Dog.objects.filter(owner=request.user)
            events = Event.objects.filter(user=request.user)
            return render(request, "d_o_profile/humanprofile.html", {
                "owner": owner, 
                "owned_dogs": owned_dogs,
                "events": events,
                })
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


# creates the view for the dog modification, using the same html of the creation view
# which was updated with needed logic to show the correct text for both scenarios.
# the id is used to capture the correct dog in the db
@login_required
def modify_dog(request, dog_id):
    dog_instance = get_object_or_404(Dog, id=dog_id)
    if request.method == "POST":
        form = DogForm(request.POST, instance=dog_instance)
        if form.is_valid():
            dog = form.save()
            return redirect(reverse('dog_profile', kwargs={'dog_id': dog_instance.id}))
    else:
        form = DogForm(instance=dog_instance)
    return render(request, 'd_o_profile/dog_profile_creation.html', {'form': form, 'dog': dog_instance})


# simple view that redirects to a confirm page and deletes the dog from the db
@login_required
def delete_dog(request, dog_id):
    dog_instance = get_object_or_404(Dog, id=dog_id)
    if request.method == "POST":
        dog_instance.delete()
        return redirect('human_profile')
    return render(request, 'd_o_profile/confirm_delete.html', {'dog': dog_instance})


# simple view to access the db of the owner and modify its data.
# it uses the owner name, which is created by the user nickname, which is unique.
@login_required
def modify_owner(request):
    owner_instance = get_object_or_404(Owner, name=request.user)
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner_instance)
        if form.is_valid():
            owner = form.save()
            return redirect('human_profile')
    else:
        form = OwnerForm(instance=owner_instance)
    return render(request, 'd_o_profile/modify_human.html', {'form': form})
