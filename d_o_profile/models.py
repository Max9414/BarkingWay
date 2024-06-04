from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Define the available choices for the age field based on average dog life
AGE_CHOICES = [(i, str(i)) for i in range(1, 21)]

#model for the db for the breeds for the dog db
class Breed(models.Model):
    breed = models.CharField(max_length=200, unique=True)

    #orders the breed in alphabetical order
    class Meta:
        ordering = ["breed"]

    #shows the breeds name instead of "object"
    def __str__(self):
        return self.breed


#model for the db for the dog's profiles
class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="dogs")
    age = models.IntegerField(choices=AGE_CHOICES)
    bitten = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    rough = models.BooleanField(default=False)

    #orders the dogs by breed first, then name
    class Meta:
        ordering = ["breed", "name"]

    #shows the dog's name and breed in the admin page
    def __str__(self):
        return f"{self.name} ({self.breed})"



