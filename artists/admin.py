from django.contrib import admin
from .models import Artist, SocialMedia


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'bio',
        'display_image',)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'facebook',
        'instagram',
        'x',
        'site',)


admin.site.register(Artist)
admin.site.register(SocialMedia, SocialMediaAdmin)
