from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Artist, SocialMedia
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArtistForm, SocialMediaForm


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


@login_required
def add_artist(request):
    """ Add an artist """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST, request.FILES)
        social_media_form = SocialMediaForm(request.POST)

        if artist_form.is_valid() and social_media_form.is_valid():
            artist = artist_form.save()

            social_media = social_media_form.save(commit=False)
            social_media.artist = artist
            social_media.save()

            messages.success(request, 'Successfully added new artist!')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to add new artist.')
    else:
        artist_form = ArtistForm()
        social_media_form = SocialMediaForm()

    template = 'artists/add_artist.html'
    context = {
        'artist_form': artist_form,
        'social_media_form': social_media_form,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """ Edit an artist profile """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST, request.FILES, instance=artist)
        social_media = SocialMedia.objects.filter(artist=artist).first()
        social_media_form = SocialMediaForm(
            request.POST, instance=social_media
        )

        if artist_form.is_valid() and social_media_form.is_valid():
            artist = artist_form.save()
            social_media = social_media_form.save()

            messages.success(request, 'Artist successfully updated')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to updated artist profile.')
    else:
        artist_form = ArtistForm(instance=artist)
        social_media_form = SocialMediaForm()
        messages.info(request, f'You are editing {artist.name}')

    template = 'artists/edit_artist.html'
    context = {
        'artist_form': artist_form,
        'social_media_form': social_media_form,
        'artist': artist,
    }

    return render(request, template, context)


@login_required
def delete_artist(request, artist_id):
    """ Delete an artist profile """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    messages.success(request, 'Artist profile deleted!')
    return redirect(reverse('products'))
