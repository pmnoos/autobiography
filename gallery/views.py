from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, "gallery/gallery.html", {"images": images})  # ✅ This will now find the correct template

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery')  # Assumes you have a named URL for the gallery
    else:
        form = GalleryImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

@login_required
def delete_image(request, image_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to delete this image.")
    image = GalleryImage.objects.get(id=image_id)
    image.delete()
    messages.success(request, "Image deleted successfully.")
    return HttpResponseRedirect(reverse('gallery:gallery'))
