from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    artist_image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    artist_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
