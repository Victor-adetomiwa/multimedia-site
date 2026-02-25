from django import forms
from .models import MediaItem

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'media_type', 'file']