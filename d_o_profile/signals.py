from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Owner

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance

    #add profile if user is created
    if created:
        Owner.objects.create(
            name=user
        )