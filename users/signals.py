from django.db.models.signals import post_save #this is a signal which gets fired after a user is created
from django.contrib.auth.models import User # signal sender
from django.dispatch import receiver # receiver of the signal
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # to craete a new profile for every new user
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):  # to craete a new profile for every new user
    instance.profile.save()
