from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    profile, upload_image, new_chapter, chapter_list, 
    chapter_detail, edit_chapter, check_grammar, about,
    search_chapters, getting_started
)

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    
    # User Profile & Password Reset
    path("profile/", profile, name="profile"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    
    # Chapters
    path("chapter/new/", new_chapter, name="new_chapter"),
    path("", chapter_list, name="chapter_list"),
    path("chapter/<slug:slug>/", chapter_detail, name="chapter_detail"),
    path("chapter/<slug:slug>/edit/", edit_chapter, name="edit_chapter"),
    path('about/', about, name='about'),
    path('getting-started/', getting_started, name='getting_started'),
    # Image Upload
    path("upload_image/", upload_image, name="upload_image"),

    # Gallery App
    path("gallery/", include("gallery.urls")),

    # Grammar Check API
    path("check_grammar/", check_grammar, name="check_grammar"),  # Changed hyphen to underscore

    # Search
    path('search/', search_chapters, name='search_chapters'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
