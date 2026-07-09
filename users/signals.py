from django.db.models.signals import post_save #A built-in Django signal that fires after a model instance is saved to the database.
from django.contrib.auth.models import User
from django.dispatch import receiver #A decorator that is used to register a function as a receiver for a specific signal. It is used to define a function that will be called when a specific signal is sent.
# pyrefly: ignore [missing-import]
from .models import profile

@receiver(post_save, sender=User) #The @receiver() decorator connects the create_profile function to the post_save signal. When a User model instance is saved (for example, when a new user registers), this signal is sent.
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
