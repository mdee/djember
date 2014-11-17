# -*- coding: utf-8 -*-

from custom_user.models import EmailUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

__author__ = 'MDee'

@receiver(post_save, sender=EmailUser)
def init_new_user(sender, instance, signal, created, **kwargs):
    """
    Create an authentication token for newly created users.
    """
    if created:
        Token.objects.create(user=instance)

