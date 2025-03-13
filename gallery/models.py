from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery_images/")  # Upload images to media/gallery_images/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
