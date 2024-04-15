from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about_game, name='about_game'),
    path('screenshots/', screenshot_page, name='screenshot_page'),
    path('video_page/', video_page, name='video_page'),
    path('audio_page/', audio_page, name='audio_page'),
    path('filtered_videos/<str:category>', filtered_videos_page, name='filtered_videos_page'),
    path('filtered_audeos/<str:category>', filtered_audeos_page, name='filtered_audeos_page'),
    path('add_page',add_page, name='add_page'),
    path('add_screen/', add_screen, name='add_screen'),
    path('add_video/', add_video, name='add_video'),
    path('add_audio/', add_audio, name='add_audio'),
]