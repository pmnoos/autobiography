"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from chapters.views import chapter_list, export_chapters_json, set_language_custom, test_view, landing_page, contact, test_autobiography, simple_test  # Ensure export_chapters_json is imported correctly
 # Ensure chapter_list is imported correctly

urlpatterns = [
    path('set_language/', set_language_custom, name='set_language'),
    path('test/', test_view, name='test'),
    path('admin/', admin.site.urls),
    path('chapters/', include('chapters.urls')),
    path("export_chapters/", export_chapters_json, name="export_chapters"),
    #path("accounts/", include("accounts.urls")), 
    path("gallery/", include(("gallery.urls", "gallery"), namespace="gallery")),
    path("", chapter_list, name="home"),  # Chapter list as homepage
    path("landing/", landing_page, name="landing"),  # Landing page moved to /landing/
    path("contact/", contact, name="contact"),  # Contact form
    # Authentication URLs
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='login', http_method_names=['get', 'post']), name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
