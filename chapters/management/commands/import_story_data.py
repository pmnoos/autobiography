from django.core.management.base import BaseCommand
from django.core import serializers
from chapters.models import Chapter
from gallery.models import GalleryImage
import json
import os

class Command(BaseCommand):
    help = 'Import story data from JSON files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--input-dir',
            type=str,
            default='story_backup',
            help='Directory containing exported data files'
        )
        parser.add_argument(
            '--clear-existing',
            action='store_true',
            help='Clear existing data before importing'
        )

    def handle(self, *args, **options):
        input_dir = options['input_dir']
        clear_existing = options['clear_existing']
        
        if not os.path.exists(input_dir):
            self.stdout.write(
                self.style.ERROR(f'Directory {input_dir} does not exist!')
            )
            return
        
        # Clear existing data if requested
        if clear_existing:
            Chapter.objects.all().delete()
            GalleryImage.objects.all().delete()
            self.stdout.write('Cleared existing data.')
        
        # Import chapters
        chapters_file = os.path.join(input_dir, 'chapters.json')
        if os.path.exists(chapters_file):
            with open(chapters_file, 'r', encoding='utf-8') as f:
                chapters_data = f.read()
            
            chapters = serializers.deserialize('json', chapters_data)
            imported_chapters = 0
            for chapter in chapters:
                chapter.save()
                imported_chapters += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Imported {imported_chapters} chapters')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Chapters file not found: {chapters_file}')
            )
        
        # Import gallery images
        gallery_file = os.path.join(input_dir, 'gallery_images.json')
        if os.path.exists(gallery_file):
            with open(gallery_file, 'r', encoding='utf-8') as f:
                gallery_data = f.read()
            
            gallery_images = serializers.deserialize('json', gallery_data)
            imported_images = 0
            for image in gallery_images:
                image.save()
                imported_images += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Imported {imported_images} gallery images')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Gallery images file not found: {gallery_file}')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Import completed!')
        ) 