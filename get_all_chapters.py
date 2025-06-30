#!/usr/bin/env python3
"""
Script to help recover ALL remaining chapters from the deployed site.
"""

import os

def create_all_chapter_files():
    """Create files for all remaining chapters to paste content into."""
    
    # All chapters based on what we know exists
    all_chapters = [
        {'slug': 'introduction', 'title': 'Introduction', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/introduction/'},
        {'slug': 'chapter1', 'title': 'Chapter 1', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter1/'},
        {'slug': 'chapter2', 'title': 'Chapter 2', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter2/'},
        {'slug': 'chapter3', 'title': 'Chapter 3', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter3/'},
        {'slug': 'chapter-4', 'title': 'Chapter 4', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter-4/'},
        {'slug': 'chapter5', 'title': 'Chapter 5', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter5/'},
        {'slug': 'chapter6', 'title': 'Chapter 6', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter6/'},
        {'slug': 'chapter7', 'title': 'Chapter 7', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter7/'},
        {'slug': 'chapter8', 'title': 'Chapter 8', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter8/'},
        {'slug': 'chapter9', 'title': 'Chapter 9', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter9/'},
        {'slug': 'chapter10', 'title': 'Chapter 10', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter10/'},
        {'slug': 'chapter11', 'title': 'Chapter 11', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter11/'},
        {'slug': 'chapter12', 'title': 'Chapter 12', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter12/'},
        {'slug': 'chapter13', 'title': 'Chapter 13', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter13/'},
        {'slug': 'chapter14', 'title': 'Chapter 14', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter14/'},
        {'slug': 'chapter15', 'title': 'Chapter 15', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter15/'},
        {'slug': 'chapter16', 'title': 'Chapter 16', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter16/'},
        {'slug': 'chapter17', 'title': 'Chapter 17', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter17/'},
        {'slug': 'chapter18', 'title': 'Chapter 18', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter18/'},
        {'slug': 'chapter19', 'title': 'Chapter 19', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter19/'},
        {'slug': 'chapter20', 'title': 'Chapter 20', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter20/'},
        {'slug': 'chapter21', 'title': 'Chapter 21', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter21/'},
        {'slug': 'chapter22', 'title': 'Chapter 22', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter22/'},
        {'slug': 'chapter23', 'title': 'Chapter 23', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter23/'},
        {'slug': 'chapter24', 'title': 'Chapter 24', 'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter24/'},
    ]
    
    # Create recovery directory
    recovery_dir = 'all_chapters_recovery'
    if not os.path.exists(recovery_dir):
        os.makedirs(recovery_dir)
    
    # Create files for each chapter
    for chapter in all_chapters:
        filename = f"{recovery_dir}/{chapter['slug']}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"""<!-- {chapter['title']} Content Recovery -->
<!-- URL: {chapter['url']} -->
<!-- 
INSTRUCTIONS:
1. Go to: {chapter['url']}
2. Right-click and "View Page Source" 
3. Copy the entire page source
4. Paste it below this comment
5. Save this file
-->

""")
    
    print(f"✅ Created {len(all_chapters)} chapter files in '{recovery_dir}/' directory")
    print("\n📋 Next Steps:")
    print("1. Go to each chapter URL listed above")
    print("2. View page source for each chapter")
    print("3. Copy and paste the content into the corresponding files")
    print("4. I'll help you extract and import ALL your story content")
    print("\n🚀 Start with Chapter 5: https://mystory-yt5w.onrender.com/chapters/chapter/chapter5/")

if __name__ == "__main__":
    create_all_chapter_files() 