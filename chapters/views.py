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
from .forms import ChapterForm  # Ensure ChapterForm exists
from django.http import JsonResponse
from django.db.models import Q
import re


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def chapter_list(request):
    chapters = Chapter.objects.all().order_by('order')  # ✅ Sort by order field

    # In commercial mode, always show welcome page for the main landing
    if getattr(settings, 'COMMERCIAL_MODE', False):
        return render(request, 'chapters/welcome.html')

    # Pagination: Show 5 chapters per page
    paginator = Paginator(chapters, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'chapters/chapter_list.html', {'page_obj': page_obj})


def chapters_list(request):
    """Separate view for displaying chapters list in commercial mode"""
    chapters = Chapter.objects.all().order_by('order')
    
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


# Grammar check functionality (placeholder for future implementation)
def check_grammar(request):
    """
    Placeholder for grammar checking functionality.
    This can be implemented later with a grammar checking service.
    """
    return JsonResponse({'errors': []})


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
