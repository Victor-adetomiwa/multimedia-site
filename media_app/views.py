from django.shortcuts import render, redirect
from .models import MediaItem
from .forms import MediaUploadForm

def home(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaUploadForm()

    items = MediaItem.objects.all()
    return render(request, 'media_app/home.html', {'items': items, 'form': form})