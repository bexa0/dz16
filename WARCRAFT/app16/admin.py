from django.contrib import admin

from app16.models import VideoCategory, AudioCategory, Screenshot, Video, Audio

# Register your models here.
admin.site.register(VideoCategory)
admin.site.register(AudioCategory)
admin.site.register(Screenshot)
admin.site.register(Video)
admin.site.register(Audio)
