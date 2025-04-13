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

from chapters.views import chapter_list, export_chapters_json  # Ensure export_chapters_json is imported correctly
 # Ensure chapter_list is imported correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapters/', include('chapters.urls')),
    #path("accounts/", include("accounts.urls")), 
    path("gallery/", include("gallery.urls")),
    path("", chapter_list, name="chapter_list"),
    path("export_chapters/", export_chapters_json, name="export_chapters"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
