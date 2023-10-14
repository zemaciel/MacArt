from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'bio',
        'display_image',)


admin.site.register(Artist)
