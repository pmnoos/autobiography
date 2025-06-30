from django.core.management.base import BaseCommand
from django.core import serializers
from chapters.models import Chapter
from gallery.models import GalleryImage
import json
import os

class Command(BaseCommand):
    help = 'Export story data to JSON files for backup/transfer'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output-dir',
            type=str,
            default='story_backup',
            help='Directory to save exported data'
        )

    def handle(self, *args, **options):
        output_dir = options['output_dir']
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Export chapters
        chapters = Chapter.objects.all()
        chapters_data = serializers.serialize('json', chapters, indent=2)
        
        with open(os.path.join(output_dir, 'chapters.json'), 'w', encoding='utf-8') as f:
            f.write(chapters_data)
        
        # Export gallery images
        gallery_images = GalleryImage.objects.all()
        gallery_data = serializers.serialize('json', gallery_images, indent=2)
        
        with open(os.path.join(output_dir, 'gallery_images.json'), 'w', encoding='utf-8') as f:
            f.write(gallery_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully exported {chapters.count()} chapters and {gallery_images.count()} gallery images to {output_dir}/')
        )
        
        # Also create a summary
        summary = {
            'chapters_count': chapters.count(),
            'gallery_images_count': gallery_images.count(),
            'chapter_titles': [chapter.title for chapter in chapters],
            'export_date': str(chapters.first().created_at) if chapters.exists() else 'No data'
        }
        
        with open(os.path.join(output_dir, 'summary.json'), 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        self.stdout.write(
            self.style.SUCCESS(f'Summary saved to {output_dir}/summary.json')
        ) 