from django.core.management.base import BaseCommand
from chapters.models import Chapter

class Command(BaseCommand):
    help = 'Load sample chapters for demo purposes.'

    def handle(self, *args, **kwargs):
        chapters = [
            {
                "title": "My Early Years",
                "subtitle": "Childhood Memories",
                "content": "I was born in a small town surrounded by rolling hills and friendly neighbors. My earliest memories are of playing in the garden, chasing butterflies, and listening to my grandmother's stories by the fireplace. School days were filled with curiosity and laughter, and I learned the value of friendship and kindness from an early age.",
                "order": 1,
            },
            {
                "title": "Adventures Abroad",
                "subtitle": "Exploring the World",
                "content": "After finishing school, I set out to see the world. My travels took me from the bustling streets of Paris to the tranquil beaches of Thailand. Each new place brought fresh experiences, new friends, and a deeper understanding of different cultures. Traveling taught me to be adaptable, open-minded, and grateful for the beauty of our planet.",
                "order": 2,
            },
            {
                "title": "Family and Friends",
                "subtitle": "The Heart of My Story",
                "content": "Family has always been my anchor. From Sunday dinners to holiday celebrations, the warmth and support of my loved ones have shaped who I am. My friends have been my companions on life's journey, sharing in both the joys and the challenges. Together, we've created memories that will last a lifetime.",
                "order": 3,
            },
            {
                "title": "Lessons Learned",
                "subtitle": "Wisdom Gained",
                "content": "Life has taught me many lessons—some easy, some hard. I've learned that perseverance pays off, that kindness matters, and that it's okay to ask for help. Every setback was a setup for a comeback, and every mistake was a chance to grow. I hope my story inspires others to embrace their own journey with courage and hope.",
                "order": 4,
            },
            {
                "title": "Looking Forward",
                "subtitle": "Dreams for the Future",
                "content": "As I look to the future, I am filled with hope and excitement. There are still places to explore, goals to achieve, and stories to write. I believe the best chapters are yet to come, and I am grateful for every moment that has brought me to where I am today.",
                "order": 5,
            },
        ]
        for ch in chapters:
            Chapter.objects.get_or_create(**ch)
        self.stdout.write(self.style.SUCCESS('Sample chapters created!'))
        self.stdout.write(self.style.WARNING('Sample images: Please upload via admin or add code for automation.')) 