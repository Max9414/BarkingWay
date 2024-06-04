from django.shortcuts import render
from django.views import generic
from .models import Dog, Owner
from django.contrib.auth.models import User

# Create your views here.

def human_profile_view(request):
    profile = request.owner.profile
    return render(request, 'd_o_profile/humanprofile.html', {'profile':profile})
