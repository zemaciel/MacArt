from django.shortcuts import render, get_object_or_404
from .models import Artist, SocialMedia



def all_artists(request):
    """ A view to show all artists """

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)


def artist_detail(request, artist_id):
    """ A view to show individual artist details """

    artist = get_object_or_404(Artist, pk=artist_id)
    social_media = SocialMedia.objects.filter(artist=artist).first()

    context = {
        'artist': artist,
        'social_media': social_media,
    }

    return render(request, 'artists/artist_detail.html', context)
