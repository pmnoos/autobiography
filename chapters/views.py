import os
import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from .models import Chapter
from .forms import ChapterForm, ContactForm  # Ensure ChapterForm exists
from django.http import JsonResponse
from django.db.models import Q
import re
from django.http import HttpResponseRedirect
from django.urls import reverse

# Simple translation dictionary
TRANSLATIONS = {
    'en': {
        'home': 'Home',
        'getting_started': 'Getting Started',
        'new_chapter': 'New Chapter',
        'photo_gallery': 'Photo Gallery',
        'upload_images': 'Upload Images',
        'admin_panel': 'Admin Panel',
        'download_backup': 'Download Backup',
        'login': 'Login',
        'logout': 'Logout',
        'welcome': 'Welcome',
        'your_life_story': 'Your Life Story - Beautifully Told',
        'subtitle': 'Create, organize, and share your life story with chapters, photos, and memories. Turn your experiences into a beautiful digital legacy.',
        'footer_quote': 'Every life is a story worth telling. Start writing yours today.',
        'footer_signature': 'Share your journey, preserve your memories, inspire others.',
    },
    'es': {
        'home': 'Inicio',
        'getting_started': 'Comenzar',
        'new_chapter': 'Nuevo Capítulo',
        'photo_gallery': 'Galería de Fotos',
        'upload_images': 'Subir Imágenes',
        'admin_panel': 'Panel de Administración',
        'download_backup': 'Descargar Respaldo',
        'login': 'Iniciar Sesión',
        'logout': 'Cerrar Sesión',
        'welcome': 'Bienvenido',
        'your_life_story': 'Tu Historia de Vida - Hermosamente Contada',
        'subtitle': 'Crea, organiza y comparte tu historia de vida con capítulos, fotos y recuerdos. Convierte tus experiencias en un hermoso legado digital.',
        'footer_quote': 'Cada vida es una historia que vale la pena contar. Comienza a escribir la tuya hoy.',
        'footer_signature': 'Comparte tu viaje, preserva tus recuerdos, inspira a otros.',
    },
    'fr': {
        'home': 'Accueil',
        'getting_started': 'Commencer',
        'new_chapter': 'Nouveau Chapitre',
        'photo_gallery': 'Galerie Photos',
        'upload_images': 'Télécharger Images',
        'admin_panel': 'Panneau Admin',
        'download_backup': 'Télécharger Sauvegarde',
        'login': 'Connexion',
        'logout': 'Déconnexion',
        'welcome': 'Bienvenue',
        'your_life_story': 'Votre Histoire de Vie - Magnifiquement Racontee',
        'subtitle': 'Créez, organisez et partagez votre histoire de vie avec des chapitres, des photos et des souvenirs. Transformez vos expériences en un magnifique héritage numérique.',
        'footer_quote': 'Chaque vie est une histoire qui mérite d\'être racontée. Commencez à écrire la vôtre aujourd\'hui.',
        'footer_signature': 'Partagez votre voyage, préservez vos souvenirs, inspirez les autres.',
    }
}

def get_translation(key, language='en'):
    """Get translation for a given key and language"""
    return TRANSLATIONS.get(language, TRANSLATIONS['en']).get(key, key)

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def chapter_list(request):
    chapters = Chapter.objects.all().order_by('order')  # ✅ Sort by order field

    # Pagination: Show 5 chapters per page
    paginator = Paginator(chapters, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'chapters/chapter_list.html', {'page_obj': page_obj})


def chapter_detail(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)

    # Get next and previous chapters based on the 'order' field
    next_chapter = Chapter.objects.filter(order__gt=chapter.order).order_by('order').first()
    prev_chapter = Chapter.objects.filter(order__lt=chapter.order).order_by('-order').first()

    return render(
        request,
        'chapters/chapter_detail.html',
        {'chapter': chapter, 'next_chapter': next_chapter, 'prev_chapter': prev_chapter}
    )



@login_required
def new_chapter(request):
    if request.method == "POST":
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save()
            return redirect("chapter_detail", slug=chapter.slug)  # Redirect after saving
    else:
        form = ChapterForm()
    return render(request, "chapters/new_chapter.html", {"form": form})


@login_required
def edit_chapter(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)

    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form.save()
            messages.success(request, "Chapter updated successfully!")
            return redirect('chapter_detail', slug=chapter.slug)
    else:
        form = ChapterForm(instance=chapter)

    return render(request, 'chapters/edit_chapter.html', {'form': form, 'chapter': chapter})


# ✅ TinyMCE Image Upload Handler
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
        filename = str(uuid.uuid4()) + os.path.splitext(image.name)[1]  # Unique name
        image_path = os.path.join('images', filename)

        # Save image
        saved_path = default_storage.save(image_path, image)

        return JsonResponse({'location': f'{settings.MEDIA_URL}{saved_path}'})  # TinyMCE expects 'location' key
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


# Initialize the LanguageTool client


def check_grammar(request):
    text = request.POST.get('text', '')  # The text to be checked
    matches = tool.check(text)
    
    # Prepare the response
    errors = []
    for match in matches:
        errors.append({
            'message': match.message,
            'error': match.replacements,
            'offset': match.offset,
            'length': match.errorLength
        })
    
    return JsonResponse({'errors': errors})

from django.http import HttpResponse
from django.core import serializers
from .models import Chapter  # adjust if your model is in a different app

def export_chapters_json(request):
    if not request.user.is_staff:
        return HttpResponse("Unauthorized", status=403)

    chapters = Chapter.objects.all()
    data = serializers.serialize('json', chapters)
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="chapters_backup.json"'
    return response



def about(request):
    return render(request, 'chapters/about.html')

def getting_started(request):
    return render(request, 'chapters/getting_started.html')

def search_chapters(request):
    query = request.GET.get('q', '')
    chapters = Chapter.objects.none()
    
    if query:
        # Check if query contains "chapter" or "ch" followed by a number
        chapter_match = re.search(r'chapter\s*(\d+)|ch\s*(\d+)', query.lower())
        
        if chapter_match:
            # Extract the chapter number
            chapter_num = chapter_match.group(1) or chapter_match.group(2)
            try:
                chapter_num = int(chapter_num)
                # Find the specific chapter by order
                specific_chapter = Chapter.objects.filter(order=chapter_num).first()
                if specific_chapter:
                    # Search within that specific chapter's content
                    chapters = Chapter.objects.filter(
                        Q(order=chapter_num) &
                        (Q(title__icontains=query) |
                         Q(subtitle__icontains=query) |
                         Q(content__icontains=query))
                    )
                else:
                    # Chapter number not found, search all chapters
                    chapters = Chapter.objects.filter(
                        Q(title__icontains=query) |
                        Q(subtitle__icontains=query) |
                        Q(content__icontains=query)
                    )
            except ValueError:
                # If chapter number parsing fails, do regular search
                chapters = Chapter.objects.filter(
                    Q(title__icontains=query) |
                    Q(subtitle__icontains=query) |
                    Q(content__icontains=query)
                )
        else:
            # Regular search across all chapters
            chapters = Chapter.objects.filter(
                Q(title__icontains=query) |
                Q(subtitle__icontains=query) |
                Q(content__icontains=query)
            ).order_by('order')
    
    # Pagination: Show 5 chapters per page
    paginator = Paginator(chapters, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'chapters/search_results.html', {
        'page_obj': page_obj, 
        'query': query,
        'total_results': chapters.count()
    })

def set_language_custom(request):
    """Custom language switching view"""
    if request.method == 'POST':
        language = request.POST.get('language', 'en')
        if language in TRANSLATIONS:
            request.session['django_language'] = language
            # Force session save
            request.session.modified = True
        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)
    return HttpResponseRedirect('/')

def test_view(request):
    """Simple test view to debug template rendering"""
    context = {
        'test_message': 'Hello World!',
        'current_language': request.session.get('django_language', 'en'),
    }
    return render(request, 'test.html', context)

def landing_page(request):
    """Landing page view for marketing and demo purposes"""
    return render(request, 'landing.html')

def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you would typically send an email or save to database
            # For now, we'll just show a success message
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('landing')
    else:
        form = ContactForm()
    
    return render(request, 'landing.html', {'contact_form': form})
