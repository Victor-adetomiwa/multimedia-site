from django.db import models

class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('image', 'Image'),
    ]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
