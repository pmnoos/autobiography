from django.db import models
from chapters.models import Chapter

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery_images/")  # Upload images to media/gallery_images/
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # New fields for integration
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    description = models.TextField(blank=True)
    date_taken = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
