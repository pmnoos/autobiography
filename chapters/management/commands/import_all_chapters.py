from django.core.management.base import BaseCommand
from chapters.models import Chapter
import os
import re
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Import all 27 chapters from pasted HTML content'

    def extract_content_from_html(self, html_content):
        """Extract title, subtitle, and content from HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract title from the chapter detail section
        title = ""
        title_elem = soup.find('div', class_='w3-display-middle')
        if title_elem:
            h1_elem = title_elem.find('h1')
            if h1_elem:
                title = h1_elem.get_text(strip=True)
        
        # Extract subtitle from h2 in chapter-detail
        subtitle = ""
        subtitle_elem = soup.find('div', class_='chapter-detail')
        if subtitle_elem:
            h2_elem = subtitle_elem.find('h2')
            if h2_elem:
                subtitle = h2_elem.get_text(strip=True)
        
        # Extract main content from div with class 'content'
        content = ""
        content_div = soup.find('div', class_='content')
        if content_div:
            content = str(content_div)
        
        return title, subtitle, content

    def handle(self, *args, **options):
        recovery_dir = 'all_chapters_recovery'
        
        if not os.path.exists(recovery_dir):
            self.stdout.write(
                self.style.ERROR(f'Directory {recovery_dir} does not exist!')
            )
            return
        
        # Clear existing chapters
        Chapter.objects.all().delete()
        self.stdout.write('Cleared existing chapters.')
        
        # Define chapter order and file mappings
        chapters_to_import = [
            {'file': 'introduction.html', 'order': 1, 'title': 'Introduction'},
            {'file': 'chapter1.html', 'order': 2, 'title': 'Chapter 1'},
            {'file': 'chapter2.html', 'order': 3, 'title': 'Chapter 2'},
            {'file': 'chapter3.html', 'order': 4, 'title': 'Chapter 3'},
            {'file': 'chapter-4.html', 'order': 5, 'title': 'Chapter 4'},
            {'file': 'chapter5.html', 'order': 6, 'title': 'Chapter 5'},
            {'file': 'chapter6.html', 'order': 7, 'title': 'Chapter 6'},
            {'file': 'chapter7.html', 'order': 8, 'title': 'Chapter 7'},
            {'file': 'chapter8.html', 'order': 9, 'title': 'Chapter 8'},
            {'file': 'chapter9.html', 'order': 10, 'title': 'Chapter 9'},
            {'file': 'chapter10.html', 'order': 11, 'title': 'Chapter 10'},
            {'file': 'chapter11.html', 'order': 12, 'title': 'Chapter 11'},
            {'file': 'chapter12.html', 'order': 13, 'title': 'Chapter 12'},
            {'file': 'chapter13.html', 'order': 14, 'title': 'Chapter 13'},
            {'file': 'chapter14.html', 'order': 15, 'title': 'Chapter 14'},
            {'file': 'chapter15.html', 'order': 16, 'title': 'Chapter 15'},
            {'file': 'chapter16.html', 'order': 17, 'title': 'Chapter 16'},
            {'file': 'chapter17.html', 'order': 18, 'title': 'Chapter 17'},
            {'file': 'chapter18.html', 'order': 19, 'title': 'Chapter 18'},
            {'file': 'chapter19.html', 'order': 20, 'title': 'Chapter 19'},
            {'file': 'chapter20.html', 'order': 21, 'title': 'Chapter 20'},
            {'file': 'chapter21.html', 'order': 22, 'title': 'Chapter 21'},
            {'file': 'chapter22.html', 'order': 23, 'title': 'Chapter 22'},
            {'file': 'chapter23.html', 'order': 24, 'title': 'Chapter 23'},
            {'file': 'chapter24.html', 'order': 25, 'title': 'Chapter 24'},
            {'file': 'chapter25.html', 'order': 26, 'title': 'Chapter 25'},
            {'file': 'chapter26.html', 'order': 27, 'title': 'Chapter 26'},
        ]
        
        imported_count = 0
        
        for chapter_info in chapters_to_import:
            file_path = os.path.join(recovery_dir, chapter_info['file'])
            
            if not os.path.exists(file_path):
                self.stdout.write(
                    self.style.WARNING(f'File not found: {chapter_info["file"]}')
                )
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Skip if file only contains instructions (small file)
                if len(html_content) < 1000:
                    self.stdout.write(
                        self.style.WARNING(f'File appears empty: {chapter_info["file"]}')
                    )
                    continue
                
                # Extract content
                extracted_title, extracted_subtitle, extracted_content = self.extract_content_from_html(html_content)
                
                # Use extracted title if available, otherwise use default
                title = extracted_title if extracted_title else chapter_info['title']
                subtitle = extracted_subtitle
                content = extracted_content
                
                # Create chapter
                Chapter.objects.create(
                    title=title,
                    subtitle=subtitle,
                    content=content,
                    order=chapter_info['order']
                )
                
                imported_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Imported: {title}')
                )
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error importing {chapter_info["file"]}: {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Successfully imported {imported_count} chapters!')
        )
        self.stdout.write(
            self.style.SUCCESS('🎉 Your complete autobiography is now restored locally!')
        ) 