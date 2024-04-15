from django.shortcuts import render
from .form import AddVideo, AddScreen, AddAudio
from .models import Screenshot, VideoCategory, Video, AudioCategory, Audio


def index(request):
    return render(request, 'index.html')


def about_game(request):
    return render(request, 'about_game.html')


def screenshot_page(request):
    context = {'screenshots': Screenshot.objects.all()}
    return render(request, 'screenshots.html', context)


def video_page(request):
    context = {'videos': VideoCategory.objects.all()}
    return render(request, 'video_page.html', context)


def filtered_videos_page(request, category):
    context = {'filtered_videos': Video.objects.filter(category=VideoCategory.objects.get(title=category))}
    return render(request, 'filtered_videos.html', context)


def audio_page(request):
    context = {'audios': AudioCategory.objects.all()}
    return render(request, 'audio_page.html', context)


def filtered_audeos_page(request, category):
    context = {'filtered_audios': Audio.objects.filter(category=AudioCategory.objects.get(title=category))}
    return render(request, 'filtered_audios.html', context)


def add_page(request):
    return render(request, 'add_page.html')


def add_screen(request):
    if request.method == 'POST':
        form = AddScreen(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Pidor")
    form = AddScreen()
    context = {'form': form}
    return render(request, 'add_screen.html', context)


def add_video(request):
    if request.method == 'POST':
        form = AddVideo(request.POST, request.FILES)
        if form.is_not_valid():
            form.save()
    form = AddVideo()
    context = {'form': form}
    return render(request, 'add_video.html', context)


def add_audio(request):
    if request.method == 'POST':
        form = AddAudio(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = AddAudio()
    context = {'form': form}
    return render(request, 'add_audio.html', context)

