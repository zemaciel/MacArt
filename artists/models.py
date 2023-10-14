from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    artist_image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    artist_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
