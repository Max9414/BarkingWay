from django.shortcuts import render
from django.views import generic
from .models import Dog
from django.contrib.auth.models import User

# Create your views here.
class Profile(generic.ListView):
    model = User