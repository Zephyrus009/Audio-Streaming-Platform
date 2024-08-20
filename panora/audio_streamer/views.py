from django.shortcuts import render
from .models import Album, album_songs

# Create your views here.

def panora_home(request):
    albums = Album.objects.all()
    return render(request,'audio_streamer/audio_home.html',{'albums':albums})

def panora_album_list(request):
    album_title = request.POST.get('album_title')
    al_songs = album_songs.objects.filter(album_title = album_title)
    albums = Album.objects.get(album_title = album_title)
    return render(request,'audio_streamer/song_list.html',{'album_songs':al_songs,'albums':albums})

def panora_player(request):
    album_title = request.POST.get('album_title')
    song_title = request.POST.get('song_name')
    play_song = album_songs.objects.get(song_title = song_title)
    albums = Album.objects.get(album_title = album_title)
    return render(request,'audio_streamer/player_screen.html',{'audio':play_song,'albums':albums})
