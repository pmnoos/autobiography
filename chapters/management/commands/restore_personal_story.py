from django.core.management.base import BaseCommand
from chapters.models import Chapter

class Command(BaseCommand):
    help = 'Restore personal story with actual content from live site.'

    def handle(self, *args, **kwargs):
        # Clear existing chapters first
        Chapter.objects.all().delete()
        
        chapters = [
            {
                "title": "Introduction",
                "subtitle": "",
                "content": "<p>I don't normally read books, but being alone for these past months has led me to seek solace in the local library. Upon entering, I was struck by its great location and the vast array of books it held. I wandered through the different categories and stumbled upon autobiographies. Despite never having delved into autobiographical works before, I thought, why not? They're factual and potentially interesting.</p><p>So, I selected one about a person whom I've long admired and found myself thoroughly engrossed in every chapter. This experience reignited my passion for reading. However, I couldn't help but notice that all the autobiographies available were about well-known figures—celebrities, if you will. It made me wonder, would anyone be interested in the life story of an ordinary person?</p><p>Now, as the end of May 2024 approaches and I find myself at the age of 85, feeling more like 65, I've come to realize that age is just a number. Inspired by the stories I've encountered, I pondered whether my own life experiences hold any value or interest to others. Thus, while awaiting the return of my partner and in an effort to keep myself occupied, I've decided to embark on recounting my story.</p><p>To anyone reading this, I wish you luck. You may find yourself either thoroughly bored or perhaps uncovering some meaningful message within my writings. Either way, I extend my best wishes to you. Good luck.</p>",
                "order": 1,
            },
            {
                "title": "Chapter 1",
                "subtitle": "116 Antrobus Rd, The Royal Town of Sutton Coldfield, Birmingham, UK. King Henry VIII granted Sutton Coldfield the \"Royal\" designation in 1528.",
                "content": "<p>What a time to have arrived on this earth! World War Two had just erupted in September 1939, plunging the world into chaos and uncertainty. As the United Kingdom was reluctantly drawn into another global conflict, families across the nation faced the grim reality of separation, sacrifice, and survival. Amidst the turmoil of war, amidst the echoes of distant battles and the shadows of impending danger, a new life entered the world, destined to navigate the challenges and opportunities of a tumultuous era. On my arrival, I joined Mother & Father and three brothers: Michael, born in 1933; Lionel, in 1934; and David, in 1936. According to my birth certificate, my father's occupation was listed as a \"Businessman,\" a title that conjures up all sorts of images of success, power, and ambition. However, as I grew older and came to know him better, I discovered that he was much more than that. He was a lovable, kind-hearted man, adored by all who knew him. With his infectious charm and gift of gab, he could light up any room and make even the most mundane moments memorable. Despite facing the challenges of being of the Jewish faith, he carried himself with dignity and resilience, embodying the values of compassion and perseverance. Unfortunately, he passed away in September 1951 when I was only eleven years old. But in all my time with him, he taught me the value of integrity, compassion, and hard work, shaping me into the person I am today. His legacy lives on in the lessons he imparted and the love he shared, guiding me through life's journey with his enduring wisdom and grace.</p>",
                "order": 2,
            },
            {
                "title": "Chapter 2",
                "subtitle": "Waltham Abby Epping The town is named and renowned for its former abbey, the last in England to be dissolved.",
                "content": "<p>The forest of Epping, nestled in Waltham Abbey, is not only a sanctuary for diverse wildlife, such as deer, foxes, and birds, but also a haven for history enthusiasts, boasting ancient relics like the ruins of Waltham Abbey, dating back to the 12th century. Despite its tranquil allure, the forest bore witness to the tumultuous years of war, with numerous military bases dotting its landscape. Amidst the serene ambiance, the sight of army trucks and soldiers underscored the gravity of the era. Additionally, the presence of a dedicated army of land girls, young women aiding in agricultural and horticultural endeavors, added to the tapestry of wartime life. As a mere infant at the time, my memories of Waltham Abbey during these years are fleeting, with only a vague recollection of an accident lingering in my mind.</p>",
                "order": 3,
            },
            {
                "title": "Chapter 3",
                "subtitle": "DOVER is a town and major ferry port in Kent, South East England. It faces France across the Strait of Dover.",
                "content": "<p>I found this Movie of Dover it will give you a good idea what Dover was like just after the war. Mum and Dad were entrepreneurs; they were the first to obtain a hotelier's license in Dover after the war. With this, they opened \"Clare House\" and operated a guesthouse at 138 Folkestone, Dover. This establishment marked the beginning of my childhood memories, preceding our departure from Epping. The reunion with our sons and brothers filled us with joy, as the war had ended, although rationing still persisted for most foods.</p><p>I believe Mum and Dad ventured into the hospitality industry due to the availability of extra rationing coupons, providing them with resources to sustain their business. Naturally, this aspect of our family's affairs was kept discreet, not to be discussed outside our family circle. With the extra rationing coupons acquired for the hotel business, Dad managed to obtain fuel for a vehicle a Vauxhall, from what I remember. It resembled an ex-army vehicle, likely one that served military personnel during the war. Its spacious interior accommodated all of us boys, along with Mum, with Dad at the wheel. We embarked on day trips, exploring the countryside and visiting quaint villages. Occasionally, Dad would pull over at a cozy pub, where we enjoyed refreshing lemonades while Mum and Dad indulged in their favorite drinks.</p>",
                "order": 4,
            },
            {
                "title": "Chapter 4",
                "subtitle": "Growing Up in Dover Dover in the 1950s remained scarred by the ravages of war, with bomb sites and debris still littering the landscape long after the conflict had ceased...",
                "content": "<p>After being given the all-clear from the hospital, signifying that I was no longer infectious due to the successful eradication of the ringworm, I returned home to clare House. I still had to wear something on my head as I was bald from having all my hair removed to treat the ringworm, although it was starting to show some growth as each day passed, with stubble beginning to appear. Resuming my education meant that returning to the boarding school was no longer an option. David was no longer there, much to his delight at being back home. However, after a week or so, I found myself being taken to another school, The Manor House Day School in Hythe.</p><p>Life during that time held its own blend of joys and sorrows. While weekdays were spent immersed in a school that captured my heart, weekends offered solace among the few friends I had made at 167 Folkestone Road. However, the shadow of poverty loomed over the streets surrounding clare House, particularly Clarendon Street and Clarendon Place, where terraced houses lined the roads, punctuated only by corner shops and the occasional chippie.</p>",
                "order": 5,
            },
        ]
        
        for ch in chapters:
            Chapter.objects.get_or_create(**ch)
        
        self.stdout.write(
            self.style.SUCCESS('✅ Your personal story has been restored successfully!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'✅ Created {len(chapters)} chapters with your actual content')
        )
        self.stdout.write(
            self.style.SUCCESS('✅ Your personal photos are already restored from git')
        )
        self.stdout.write(
            self.style.SUCCESS('🎉 Your autobiography is now back in your local development environment!')
        ) 