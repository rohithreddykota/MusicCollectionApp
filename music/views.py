from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# , get_list_or_404
from .models import Album, Songs
from django.db.models import Q
# from django.shortcuts import redirect
# from django.core.urlresolveers import reverse


def search_songs(songs, query):
    songs = songs.filter( Q(song_title__icontains = query))
    return songs
	 

def login_user(request):
    if request.POST or request.GET:
        return redirect('music:index')
    return render(request, 'music/login_user.html')


def index(request):
    albums = Album.objects.all()
    query = request.GET.get("query")
    if query:
        albums = albums.filter(
            Q(album_title__icontains=query) |
            Q(artist__icontains=query)
        )
    return render(request, 'music/index.html', {'albums': albums})


def details(request, album_id):
    album = Album.objects.get(pk=album_id)
    songs = album.songs_set.all()
    query = request.GET.get('query')
    if query:
        songs = search_songs(songs,query)
    return render(request, 'music/details.html', {'songs': songs, 'album': album})


def all_songs(request):
    songs = Songs.objects.all()
    query = request.GET.get('query')
    if query:
        songs = search_songs(songs,query)
    return render(request, 'music/all_songs.html', {'songs': songs})


def all_favorite_songs(request):
    songs = Songs.objects.filter(isfavorite=1)
    query = request.GET.get('query')
    if query:
        songs = search_songs(songs,query)
    return render(request, 'music/all_favorite_songs.html', {'songs': songs})


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('music:index')
    # return render(request, 'music/index.html')


def delete_song(request, song_id):
    song = get_object_or_404(Songs, pk=song_id)
    album_id = song.album.id
    song.delete()
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return redirect(previous_url)
    return redirect('music:details', album_id)


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.isfavorite = not album.isfavorite
    album.save()
    return redirect('music:index')
    # return render(request, 'music/index.html')


def favorite_song(request, song_id):
    song = get_object_or_404(Songs, pk=song_id)
    song.isfavorite = not song.isfavorite
    song.save()
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return redirect(previous_url)
    args = (song.album.id,)
    return redirect('music:details', *args)


def home(request):
    return HttpResponse('this is home page')


def logout_user(request):
    pass
