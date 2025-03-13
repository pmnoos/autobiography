from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField  # Use this directly

class Chapter(models.Model):
    title = models.CharField(max_length=255, blank=False)
    subtitle = models.TextField(blank=True, null=True)
    content = HTMLField(blank=True, null=True)  # Use TinyMCE's rich text field
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track updates
    order = models.IntegerField(default=999)  # Field to control display order

    def save(self, *args, **kwargs):
        # Ensure unique slug by appending order or ID if needed
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Chapter.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        
        # Auto-assign order if not set
        if not self.order or self.order == 999:
            last_chapter = Chapter.objects.order_by('-order').first()
            self.order = (last_chapter.order + 1) if last_chapter else 1
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}: {self.title}"
