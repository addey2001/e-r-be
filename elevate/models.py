from django.db import models
from django.conf import settings

class Listing(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    description = models.TextField()
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_listings', blank=True)

    def __str__(self):
        return f"{self.description[:30]} ({self.location})"
