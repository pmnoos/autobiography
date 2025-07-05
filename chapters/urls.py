from django.urls import path, include

from .views import (
    profile, upload_image, new_chapter, chapter_list, 
    chapter_detail, edit_chapter, check_grammar, about,
    search_chapters, getting_started
)

urlpatterns = [
    # User Profile & Password Reset
    path("profile/", profile, name="profile"),
    
    # Chapters
    path("chapter/new/", new_chapter, name="new_chapter"),
    path("", chapter_list, name="chapter_list"),
    path("chapter/<slug:slug>/", chapter_detail, name="chapter_detail"),
    path("chapter/<slug:slug>/edit/", edit_chapter, name="edit_chapter"),
    path('about/', about, name='about'),
    path('getting-started/', getting_started, name='getting_started'),
    # Image Upload
    path("upload_image/", upload_image, name="upload_image"),

    # Gallery App - Removed duplicate URL pattern (already defined in core/urls.py)

    # Grammar Check API
    path("check_grammar/", check_grammar, name="check_grammar"),  # Changed hyphen to underscore

    # Search
    path('search/', search_chapters, name='search_chapters'),
]

# Serve media files in development mode
