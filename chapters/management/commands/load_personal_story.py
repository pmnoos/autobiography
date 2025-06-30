from django.core.management.base import BaseCommand
from chapters.models import Chapter

class Command(BaseCommand):
    help = 'Load personal story chapters.'

    def handle(self, *args, **kwargs):
        # Clear existing chapters first
        Chapter.objects.all().delete()
        
        chapters = [
            {
                "title": "My Life Story",
                "subtitle": "My Personal Journey",
                "content": """
                <p>Welcome to my personal memoir. This is where my story begins - a collection of memories, experiences, and lessons learned throughout my life's journey.</p>
                
                <p>I've always believed that everyone has a story worth telling. This is mine - a digital memoir of the moments that have shaped me, the people who have influenced me, and the experiences that have made me who I am today.</p>
                
                <p>From childhood memories to adult adventures, from challenges overcome to dreams pursued, this is my attempt to capture the essence of my life's journey. I hope that sharing these stories will not only preserve my memories but also inspire others to reflect on their own life stories.</p>
                
                <p>Each chapter represents a different phase of my life, filled with both the ordinary moments that make life beautiful and the extraordinary experiences that make it memorable.</p>
                """,
                "order": 1,
            },
            {
                "title": "Early Years",
                "subtitle": "Childhood and Family",
                "content": """
                <p>My earliest memories are filled with the warmth of family and the innocence of childhood. Growing up in [Your hometown], I was surrounded by love, laughter, and the simple joys of discovery.</p>
                
                <p>My family played a central role in shaping my values and beliefs. My parents taught me the importance of hard work, kindness, and perseverance. My siblings were my first friends and companions in adventure.</p>
                
                <p>School days were a mix of learning, friendship, and growing up. I remember the excitement of new discoveries, the comfort of familiar routines, and the bonds formed with classmates who would become lifelong friends.</p>
                
                <p>These early years laid the foundation for everything that would follow - my curiosity about the world, my love for learning, and my appreciation for the people who make life meaningful.</p>
                """,
                "order": 2,
            },
            {
                "title": "Growing Up",
                "subtitle": "Teenage Years and Discovery",
                "content": """
                <p>The teenage years brought new challenges and opportunities for growth. It was a time of self-discovery, of questioning, and of finding my own path in the world.</p>
                
                <p>High school introduced me to new subjects, new people, and new possibilities. I discovered interests that would shape my future - whether it was a particular subject that fascinated me, a hobby that brought me joy, or a cause that inspired me to action.</p>
                
                <p>Friendships deepened and changed, relationships with family evolved, and I began to understand more about who I was and who I wanted to become.</p>
                
                <p>These years were marked by both the typical struggles of adolescence and the unique experiences that made my journey my own. Looking back, I can see how each experience, whether positive or challenging, contributed to my growth and development.</p>
                """,
                "order": 3,
            },
            {
                "title": "Adulthood and Career",
                "subtitle": "Building a Life",
                "content": """
                <p>Entering adulthood brought new responsibilities and opportunities. I faced decisions about education, career, and the kind of life I wanted to build for myself.</p>
                
                <p>My career path has been a journey of its own - filled with learning, growth, challenges overcome, and achievements celebrated. Each job, each project, each colleague has taught me something valuable about work, about people, and about myself.</p>
                
                <p>Alongside my professional life, I've continued to pursue personal interests, maintain relationships, and work toward goals that matter to me. Life has taught me the importance of balance, of perseverance, and of staying true to my values.</p>
                
                <p>This phase of life has been about building something meaningful - whether that's a career, relationships, or a sense of purpose and contribution to the world around me.</p>
                """,
                "order": 4,
            },
            {
                "title": "Life Lessons",
                "subtitle": "Wisdom Gained Through Experience",
                "content": """
                <p>Life has been my greatest teacher. Through both success and failure, joy and sorrow, I've learned lessons that have shaped my perspective and guided my choices.</p>
                
                <p>I've learned that resilience is more valuable than perfection, that kindness costs nothing but means everything, and that the people in our lives are our greatest wealth.</p>
                
                <p>I've discovered that failure is not the opposite of success but a stepping stone toward it. Every setback has taught me something valuable, every challenge has made me stronger, and every mistake has been an opportunity for growth.</p>
                
                <p>Perhaps most importantly, I've learned that life is not about reaching a destination but about enjoying the journey. The moments of connection, the small victories, the quiet joys - these are what make life truly rich and meaningful.</p>
                """,
                "order": 5,
            },
            {
                "title": "Looking Forward",
                "subtitle": "Dreams and Aspirations",
                "content": """
                <p>As I reflect on my journey so far, I'm filled with gratitude for all that has been and excitement for all that is yet to come.</p>
                
                <p>I still have dreams to pursue, goals to achieve, and experiences to savor. There are places I want to visit, skills I want to learn, and relationships I want to deepen.</p>
                
                <p>I hope to continue growing, learning, and contributing to the world around me. I want to be a positive force in the lives of others, to leave a legacy of kindness and purpose, and to make the most of every day I'm given.</p>
                
                <p>This memoir is not just a record of the past but a foundation for the future. It reminds me of who I am, where I've been, and what matters most to me as I continue forward on this journey called life.</p>
                
                <p>Thank you for sharing in my story. May it inspire you to reflect on your own journey and to appreciate the beautiful, complex, and meaningful story that is your life.</p>
                """,
                "order": 6,
            },
        ]
        
        for ch in chapters:
            Chapter.objects.get_or_create(**ch)
        
        self.stdout.write(
            self.style.SUCCESS('Personal story chapters created successfully!')
        )
        self.stdout.write(
            self.style.WARNING('Remember to customize the content with your actual personal stories and experiences.')
        ) 