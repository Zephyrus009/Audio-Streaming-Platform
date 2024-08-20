from django.urls import path
from . import views

app_name = 'audio_streamer'


urlpatterns = [
    path('panora_home/',views.panora_home,name = "panora_home"),
    path('panora_album_list/',views.panora_album_list,name = "panora_album_list"),
    path('panora_player/',views.panora_player,name = "panora_player"),
]
