from django import forms
from .models import Screenshot, Video, Audio


class AddScreen(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ('image',)


class AddVideo(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('category','video')
        widget = {'category': forms.MultipleChoiceField()}


class AddAudio(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('category','audio')
        widget = {'category': forms.MultipleChoiceField()}