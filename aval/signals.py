from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Avaliation


@receiver(post_save, sender=Avaliation)
def create_aval(sender, instance, created, **kwargs):
    if created:
        Avaliation.objects.create(user=instance)


@receiver(post_save, sender=Avaliation)
def save_aval(sender, instance, **kwargs):
    instance.user.save()
