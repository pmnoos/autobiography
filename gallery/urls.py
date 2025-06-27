from django.urls import path
from .views import gallery_view, upload_image, delete_image

urlpatterns = [
    path("", gallery_view, name="gallery"),
    path("upload/", upload_image, name="upload_image"),
    path("delete/<int:image_id>/", delete_image, name="delete_image"),
]