from django.conf.urls import url  # include
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
    url(r'^albums/$', views.index, name='index'),
    url(r'^favorite-songs/$', views.all_favorite_songs, name='all_favorite_songs'),
    url(r'^(?P<album_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^all-songs/$', views.all_songs, name='all_songs'),
    url(r'^(?P<album_id>[0-9]+)/delete-album/$', views.delete_album, name='delete_album'),
    url(r'^(?P<album_id>[0-9]+)/favorite-album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<song_id>[0-9]+)/favorite-song/$', views.favorite_song, name='favorite_song'),
    url(r'^(?P<song_id>[0-9]+)/delete-song/$', views.delete_song, name='delete_song'),
    url(r'^(?P<song_id>[0-9]+)/delete-song/$', views.delete_song, name='delete_song'),
    url(r'^logout-user/$', views.logout_user, name='logout_user'),
]
