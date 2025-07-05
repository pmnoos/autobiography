from django.core.management.base import BaseCommand
from chapters.models import Chapter

class Command(BaseCommand):
    help = 'Load sample chapters for demo purposes.'

    def handle(self, *args, **kwargs):
        # Clear existing chapters first
        Chapter.objects.all().delete()
        chapters = [
            {
                "title": "Welcome to LifeStory Platform",
                "subtitle": "Your Digital Memoir Journey Begins",
                "content": "Welcome to your personal life story platform. This is where your journey begins - a digital space to capture, preserve, and share the moments that have shaped your life. Whether you're writing for yourself, your family, or future generations, this platform provides the tools you need to tell your story beautifully and professionally.",
                "order": 1,
            },
            {
                "title": "Getting Started with Your Story",
                "subtitle": "How to Begin Your Autobiography",
                "content": "Starting your life story can feel overwhelming, but it doesn't have to be. Begin with the moments that matter most to you - your earliest memories, significant life events, or the people who have influenced you most. Use this platform's rich text editor to bring your stories to life with formatting, images, and personal touches that make your narrative uniquely yours.",
                "order": 2,
            },
            {
                "title": "Organizing Your Chapters",
                "subtitle": "Structuring Your Life Story",
                "content": "A well-organized autobiography helps readers follow your journey. Consider organizing your chapters chronologically, by theme, or by significant life periods. Use the order field to arrange your chapters in the sequence you want them to appear. Each chapter can include photos, memories, and reflections that bring your story to life.",
                "order": 3,
            },
            {
                "title": "Adding Photos and Memories",
                "subtitle": "Bringing Your Story to Life",
                "content": "Photographs have the power to transport readers to specific moments in time. Upload your photos through the gallery feature and link them to relevant chapters. Include captions and descriptions that provide context and enhance the storytelling experience. Your images will be displayed beautifully alongside your written content.",
                "order": 4,
            },
            {
                "title": "Sharing Your Story",
                "subtitle": "Connecting with Readers",
                "content": "Your life story is a gift to future generations and a way to connect with others who may find inspiration in your experiences. Use this platform to share your wisdom, lessons learned, and the unique perspective that only you can offer. Your story matters, and this platform helps you tell it in a way that honors your journey.",
                "order": 5,
            },
        ]
        for ch in chapters:
            Chapter.objects.get_or_create(**ch)
        self.stdout.write(self.style.SUCCESS('Sample chapters created!'))
        self.stdout.write(self.style.WARNING('Sample images: Please upload via admin or add code for automation.')) 