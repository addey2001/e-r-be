from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

from elevate.models import Listing

class User(AbstractUser):
    wishlist = models.ManyToManyField(Listing, related_name='wishlisted_by', blank=True)