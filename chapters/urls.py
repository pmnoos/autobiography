from django.urls import path, include
from . import views
from .views import profile, upload_image
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_image
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),  # Ensure this is before the slug pattern
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("profile/", profile, name="profile"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('chapter/new/', views.new_chapter, name='new_chapter'),
    path('', views.chapter_list, name='chapter_list'),
    path('chapter/<slug:slug>/', views.chapter_detail, name='chapter_detail'),
    path('chapter/<slug:slug>/edit/', views.edit_chapter, name='edit_chapter'),
    path('upload_image/', upload_image, name='upload_image'),
    path("gallery/", include("gallery.urls")), 
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)