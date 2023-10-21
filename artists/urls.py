from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('addartist/', views.add_artist, name='add_artist'),
]
