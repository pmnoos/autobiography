#!/usr/bin/env python3
"""
Script to help recover personal story chapters from the deployed site.
This will create files for each chapter that you can then copy content into.
"""

import os

def create_chapter_files():
    """Create files for each chapter to paste content into."""
    
    chapters = [
        {
            'slug': 'introduction',
            'title': 'Introduction',
            'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/introduction/'
        },
        {
            'slug': 'chapter1',
            'title': 'Chapter 1',
            'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter1/'
        },
        {
            'slug': 'chapter2', 
            'title': 'Chapter 2',
            'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter2/'
        },
        {
            'slug': 'chapter3',
            'title': 'Chapter 3', 
            'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter3/'
        },
        {
            'slug': 'chapter-4',
            'title': 'Chapter 4',
            'url': 'https://mystory-yt5w.onrender.com/chapters/chapter/chapter-4/'
        }
    ]
    
    # Create recovery directory
    recovery_dir = 'story_recovery'
    if not os.path.exists(recovery_dir):
        os.makedirs(recovery_dir)
    
    # Create files for each chapter
    for chapter in chapters:
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
    
    print(f"✅ Created {len(chapters)} chapter files in '{recovery_dir}/' directory")
    print("\n📋 Next Steps:")
    print("1. Go to each chapter URL listed above")
    print("2. View page source for each chapter")
    print("3. Copy and paste the content into the corresponding files")
    print("4. I'll help you extract and import the story content")

if __name__ == "__main__":
    create_chapter_files() 
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/introduction/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/New_Zealand_Trip_Jan_2007_002.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Introduction
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><p>&nbsp;</p>
<h1 style="text-align: center;">Introduction</h1>
<p>&nbsp;</p></h2>
        
 <hr>       
        <div class="content">
            <p>I don't normally read books, but being alone for these past months has led me to seek solace in the local library. Upon entering, I was struck by its great location and the vast array of books it held. I wandered through the different categories and stumbled upon autobiographies. Despite never having delved into autobiographical works before, I thought, why not? They're factual and potentially interesting.</p>
<p>So, I selected one about a person whom I've long admired and found myself thoroughly engrossed in every chapter. This experience reignited my passion for reading. However, I couldn't help but notice that all the autobiographies available were about well-known figures&mdash;celebrities, if you will. It made me wonder, would anyone be interested in the life story of an ordinary person?</p>
<p>Now, as the end of May 2024 approaches and I find myself at the age of 85, feeling more like 65, I've come to realize that age is just a number. Inspired by the stories I've encountered, I pondered whether my own life experiences hold any value or interest to others. Thus, while awaiting the return of my partner and in an effort to keep myself occupied, I've decided to embark on recounting my story.</p>
<p>To anyone reading this, I wish you luck. You may find yourself either thoroughly bored or perhaps uncovering some meaningful message within my writings. Either way, I extend my best wishes to you. Good luck.</p>
<p>I don't usually read books, but spending these past months alone has led me to seek solace in the local library. Upon entering, I was struck by its great location and the vast array of books it held. I wandered through different categories and stumbled upon autobiographies. Although I had never delved into autobiographical works before, I thought, why not? They're factual and potentially interesting.</p>
<p>I chose one about a person I've long admired and found myself thoroughly engrossed in every chapter. This experience reignited my passion for reading. However, I couldn&rsquo;t help but notice that all the autobiographies available were about well-known figures&mdash;celebrities, if you will. It made me wonder, would anyone be interested in the life story of an ordinary person?</p>
<p>Now, as May 2024 approaches and I find myself at the age of 85, feeling more like 65, I've come to realize that age is just a number. Inspired by the stories I've encountered, I've begun to ponder whether my own life experiences hold any value or interest to others. So, while waiting for the return of my partner and in an effort to keep myself occupied, I've decided to recount my story.</p>
<p>To anyone reading this, I wish you luck. You might find yourself thoroughly bored or perhaps uncover some meaningful message within my writings. Either way, I extend my best wishes to you. Good luck.</p>
        </div>
     
        
    
        <a href="/chapters/chapter/chapter1/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>    



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/chapter1/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/Longmoor_Pool_-_Summer_2007.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Chapter 1
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><p><strong>116 Antrobus Rd, The Royal Town of Sutton Coldfield, Birmingham, UK. King Henry VIII granted Sutton Coldfield the "Royal" designation in 1528. This recognition was due to its historical association with the Royal family and its importance as a centre of hunting grounds and woodlands used by the monarchy.</strong></p></h2>
        
 <hr>       
        <div class="content">
            <p>What a time to have arrived on this earth! World War Two had just erupted in September 1939, plunging the world into chaos and uncertainty. As the United Kingdom was reluctantly drawn into another global conflict, families across the nation faced the grim reality of separation, sacrifice, and survival. Amidst the turmoil of war, amidst the echoes of distant battles and the shadows of impending danger, a new life entered the world, destined to navigate the challenges and opportunities of a tumultuous era. On my arrival, I joined <a href="../../../media/images/dadmum.jpg" target="_blank" rel="noopener" data-lightbox="gallery">Mother &amp; Father&nbsp;</a> and three brothers: Michael, born in 1933; Lionel, in 1934; and David, in 1936. According to my birth certificate, my father's occupation was listed as a "Businessman," a title that conjures up all sorts of images of success, power, and ambition. However, as I grew older and came to know him better, I discovered that he was much more than that. He was a lovable, kind-hearted man, adored by all who knew him. With his infectious charm and gift of gab, he could light up any room and make even the most mundane moments memorable. Despite facing the challenges of being of the Jewish faith, he carried himself with dignity and resilience, embodying the values of compassion and perseverance. Unfortunately, he passed away in September 1951 when I was only eleven years old. But in all my time with him, he taught me the value of integrity, compassion, and hard work, shaping me into the person I am today. His legacy lives on in the lessons he imparted and the love he shared, guiding me through life's journey with his enduring wisdom and grace. More about my father later on, my Mother was considerably younger than my father, hailing from Dover, Kent, where my early years unfolded. A period I'll delve into in detail later. While my recollections of her during that time are limited by my tender age, the stories I've heard paint a vivid picture of her remarkable character. They say she possessed a culinary talent beyond compare, a trait I would come to appreciate fully in later years. Yet, her skills in the kitchen were merely a reflection of her boundless love and care as a mother. She dedicated herself wholeheartedly to raising her four sons, navigating the challenges of life with unwavering strength and grace. Despite the hardships she encountered, my mother remained steadfast in her commitment to our family, selflessly putting our needs above her own. Her love was the bedrock of our household, her presence a constant source of warmth and comfort. She was not only the heart of our family but also the glue that held us together through every trial and triumph. Her legacy extends far beyond her culinary creations; it lives on in the love she shared and the values she imparted. Through her example, she taught us the true meaning of resilience, compassion, and unwavering devotion. As I continue to recount my story, I look forward to delving deeper into the memories and moments that define her enduring influence on my life. My memories of Antrobus Street exist only through the stories my mother shared with me over time. It was in 1941, amidst the chaos of World War II, that our family decided to leave Antrobus Street and relocate to Waltham Abbey in London. The war was raging on, and England's vulnerability meant that bombings were a nightly occurrence, casting a shadow of fear over our lives. During this uncertain time, my brothers were evacuated to Wales for safety. As for me, I was deemed too young to leave my mother's side, so I remained in London throughout the war, not seeing my brothers until its end in 1945. The separation from my brothers and the constant threat of bombings were challenging experiences that defined my early years. Yet amidst the turmoil, there was a sense of resilience and determination to endure. My family's story, like so many others during that time, is a testament to the strength and courage of ordinary people facing extraordinary circumstances. Reflecting on these memories, I'm reminded of the sacrifices made by my family and countless others during World War II. It's a chapter of my life that shaped who I am today, instilling in me values of resilience, unity, and gratitude for the peace we now enjoy. As I continue to write my story, I honor the past and embrace the journey that has led me to where I am today.</p>
        </div>
     
        
        <a href="/chapters/chapter/introduction/" class="btn btn-secondary">Previous Chapter</a>
    
    
        <a href="/chapters/chapter/chapter2/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/chapter2/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/Epping_Forest.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Chapter 2
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><p>Waltham Abby Epping The town is named and renowned for its former abbey, the last in England to be dissolved, now the Abbey Church of Waltham Holy Cross and St Lawrence, a scheduled ancient monument, and the town's parish church.</p></h2>
        
 <hr>       
        <div class="content">
            <p>The forest of Epping, nestled in Waltham Abbey, is not only a sanctuary for diverse wildlife, such as deer, foxes, and birds, but also a haven for history enthusiasts, boasting ancient relics like the ruins of Waltham Abbey, dating back to the 12th century. Despite its tranquil allure, the forest bore witness to the tumultuous years of war, with numerous military bases dotting its landscape. Amidst the serene ambiance, the sight of army trucks and soldiers underscored the gravity of the era. Additionally, the presence of a dedicated army of land girls, young women aiding in agricultural and horticultural endeavors, added to the tapestry of wartime life. As a mere infant at the time, my memories of Waltham Abbey during these years are fleeting, with only a vague recollection of an accident lingering in my mind..<br>&nbsp; &nbsp; &nbsp; &nbsp; By all accounts, the incident unfolded swiftly as I found myself lifted by the gentle hands of a couple of these land girls, undoubtedly charmed by the innocence of a young child. Placed atop one of their bicycles, I must have presented an irresistible sight, prompting their spontaneous act of kindness.<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; As we strolled along the footpath, the tranquility of the forest was momentarily disrupted by the rumble of an approaching army convoy. Caught up in the moment, the young ladies, exuding a sense of glamour amidst the natural splendor, exchanged smiles and waves with the passing soldiers. Little did they know, nor perhaps did the soldier at the wheel realize, that protruding from the back of one of the trucks was an iron girder, concealed from view.<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; As the convoy straightened its course, the inevitable collision occurred the end of the girder meeting my unsuspecting head. The ensuing chaos unfolded in a whirlwind of confusion and concern, leaving an indelible mark on all involved<br>&nbsp; &nbsp; &nbsp; &nbsp; To this day, a faint scar on my scalp serves as a tangible reminder of life's fragility and the capricious hand of fate. Despite the gravity of the incident, the details remain shrouded in the haze of memory. Legal action was pursued on my behalf by my father, resulting in a compensation award. However, the funds were held in trust until my twenty-first birthday, marking the beginning of another tale yet to unfold.<br>&nbsp; &nbsp; &nbsp; &nbsp; The next event in my life moving down to Dover in 1947.</p>
        </div>
     
        
        <a href="/chapters/chapter/chapter1/" class="btn btn-secondary">Previous Chapter</a>
    
    
        <a href="/chapters/chapter/chapter3/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/chapter3/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/dover.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Chapter 3
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><p>DOVER is a town and major ferry port in Kent, South East England. It faces France across the Strait of Dover, the narrowest part of the English Channel at 33 kilometres (21 mi) from Cap Gris Nez in France.</p></h2>
        
 <hr>       
        <div class="content">
            <p>I found this&nbsp;<a title="Movie of Dover" href="https://www.youtube.com/watch?v=jP0QRTP554s" target="_blank" rel="noopener">Movie of Dover</a> it will give you a good idea what Dover was like just after the war.Mum and Dad were entrepreneurs; they were the first to obtain a hotelier's license in Dover after the war. With this, they opened "Clare House" and operated a guesthouse at 138 Folkestone, Dover. This establishment marked the beginning of my childhood memories, preceding our departure from Epping. The reunion with our sons and brothers filled us with joy, as the war had ended, although rationing still persisted for most foods.</p>
<p>&nbsp;I believe Mum and Dad ventured into the hospitality industry due to the availability of extra rationing coupons, providing them with resources to sustain their business. Naturally, this aspect of our family's affairs was kept discreet, not to be discussed outside our family circle. With the extra rationing coupons acquired for the hotel business, Dad managed to obtain fuel for a vehicle a Vauxhall, from what I remember. It resembled an ex-army vehicle, likely one that served military personnel during the war. Its spacious interior accommodated all of us boys, along with Mum, with Dad at the wheel. We embarked on day trips, exploring the countryside and visiting quaint villages. Occasionally, Dad would pull over at a cozy pub, where we enjoyed refreshing lemonades while Mum and Dad indulged in their favorite drinks.</p>
<p>&nbsp;One memorable occasion stands out: when we visited Dad's relatives in Eastbourne. It marked my introduction to Jewish cuisine at the tender age of seven. The table was adorned with delicacies like smoked salmon, rollmops, matzos, anchovies, and potato salad. This culinary experience sparked my lifelong love for fine foods, igniting a passion at a young age.&nbsp; With the reopening of the channel, Dover bustled with activity as people flocked to use the cross-channel ferries. This surge in visitors kept Mum and Dad busy at the guesthouse. After about a year, ever the one to seek improvement, Dad decided to relocate us to a larger residence, providing more rooms for guests. Thus, we packed our belongings and moved across the road to 167 Folkestone Road.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>It was during this time that I grew particularly close to<a href="../../../media/images/mydad.jpg"> My Dad</a><a title="My Dad" href="static/media/images/mydad.jpg" target="_blank" rel="noopener"> </a>my father. I often accompanied him on his shopping trips, eagerly climbing into our beloved Vauxhall. I felt a sense of pride every time I stepped into the car, especially considering that owning a car alone was enough to turn heads at that time. Dad also acquired a little dog, Rex, a crossbreed of unknown origin. Whenever Rex was in the back of the car, he was fiercely protective, barking at anyone who dared approach the vehicle. Dad found solace in knowing Rex was there, ensuring our safety. On our shopping trips back then, supermarkets where you could buy all you need in one place didn't exist. Instead, we frequented local shops a butcher, grocer, fruiterer, and even farms for fresh chicken. I mean really fresh Dad would choose one, and the farmer would promptly prepare it while it was still running around, ending its life in front of us. But let's get back to the shopping.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>Dad would stride into these stores with me following in awe. "Hi, Morrie!" Each manager would emerge from their office to greet him, extending their hand for a handshake. This ritual occurred every visit, and there I was, a little me, following in his footsteps. It was the best feeling for me. I was bursting with pride for my father. Though I didn't fully grasp what pride meant at that age, I was in awe and loved him immensely. With each time returning to our vehicle, the car boot was full of different kinds of food In all my childhood memories, this period stands out as the best for me. The parties Mum and Dad threw for their friends and business colleagues were brilliant. From a young age, I observed a diverse array of people from various occupations attending these gatherings. While my brothers and I were included to a certain extent, as the parties progressed into the evening, we were gently dismissed to our bedtime!<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Despite being relegated to our rooms, the energy and excitement of the parties lingered in the air, leaving an indelible impression on my young mind. From the laughter and music to the tantalizing aroma of food, these were a testament to our parents' hospitality and social prowess. Though we may have been tucked away in bed, the memories of those lively gatherings remain etched in my heart.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Another memory I have of my father involves him in the kitchen, always cooking something up for us boys. Whenever the front doorbell rang, he would hurriedly make his way to answer it, donning his oversized white apron. With a quick flick, he would fold back one corner of the apron as if it weren't there at all. Upon greeting whoever stood at the door, he would immediately tune into their accent or language, effortlessly imitating them. This knack for mimicry endeared him to everyone he met, fostering instant rapport and camaraderie. He had a remarkable ability to connect with people from all walks of life, a talent that earned him admiration and respect. In my eyes, he could sell ice to the Eskimos.My schooling journey began with attendance at three primary schools. The first was Belgrave Primary, situated right opposite the first clare House atop a steep hill. My memories of it are fleeting, but I distinctly recall its location across a busy road.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Next was St. Mary's Primary in Stembrock, a district in the downtown area. Although I can't recall the duration of my stay, both schools were housed in ancient buildings.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; The third, St. Martins Primary in Elms Vale, remains vivid. I found enjoyment there, as it boasted modern facilities compared to the previous two. However, I encountered a challenging experience with an English teacher. During a test, sunlight streaming into the room made the blackboard unreadable. When I leaned forward to get a better view, the teacher accused me of cheating. Despite my protests, the situation escalated, leading to my departure from the school. Fortunately, my father believed my account of the incident.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Meanwhile, my brothers Michael and Lionel were old enough to apply to join the Royal Navy HMS Mercury training school. David must have been attending a school in Dover.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Subsequently, David and I were enrolled in Horam boarding school for boys near Hailsham, Sussex. The school boasted excellent teachers and picturesque grounds. The Principal, a passionate butterfly collector, nurtured my interest in entomology. Despite the pleasant environment, I struggled with the mandatory Sunday tea of macaroni cheese and goat's milk, leading to clandestine food exchanges among dormitory mates.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; However, my time at the boarding school was short-lived due to a severe case of ringworm. Placed in quarantine, I stayed with an Uncle and Auntie nearby for three months, undergoing treatment at Middlesex Hospital. Despite efforts to cure the ringworm, it persisted, resulting in the nurses' manually removing each affected hair, a process I endured longer than any other patient.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; During my absence, my nephew Peter was with us at the boarding school. He was briefly sent to stay with me at our relatives, but his parents promptly retrieved him. Consequently, I found myself residing with unfamiliar relatives who imposed strict rules, possibly due to my infectious condition.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Looking back, my schooling years so far were a mixed bag of challenges and memorable experiences, shaping me in unexpected ways.</p>
<p>&nbsp; In December 1950, a new addition to the family arrived: my little brother, Phillip. With his arrival, the Magner family grew to include five boys. Additionally, I took on the responsibility of caring for Phillip during his early years, a role I can elaborate on later.</p>
        </div>
     
        
        <a href="/chapters/chapter/chapter2/" class="btn btn-secondary">Previous Chapter</a>
    
    
        <a href="/chapters/chapter/chapter-4/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/chapter-4/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/bombsites_tBrIiZG.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Chapter 4
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><h3 class="subtitle-section">Growing Up in Dover Dover in the 1950s remained scarred by the ravages of war, with bomb sites and debris still littering the landscape long after the conflict had ceased...</h3></h2>
        
 <hr>       
        <div class="content">
            <p>After being given the all-clear from the hospital, signifying that I was no longer infectious due to the successful eradication of the ringworm, I returned home to clare House. I still had to wear something on my head as I was bald from having all my hair removed to treat the ringworm, although it was starting to show some growth as each day passed, with stubble beginning to appear. Resuming my education meant that returning to the boarding school was no longer an option. David was no longer there, much to his delight at being back home. However, after a week or so, I found myself being taken to another school, The Manor House Day School in Hythe.<br>The school was situated in a literally Manor House, a grand mansion set amidst wonderful grounds, surrounded by an amazing array of different plants, bushes, and trees. There was even a very old-looking Mulberry tree that was fruiting at the time of my visit. The uniform we had to wear was a bright red, almost scarlet, peaked cap, along with a single-breasted blazer and gray flannel trousers. I loved it! There was just one slight problem with attending this wonderful school it was about 25 miles from clare House, and there was nobody available to take me there or bring me back home. However, my father, on the way home from our visit to the school, drove me to the Folkestone bus station and showed me how we could overcome this problem. On school days, I would don my bright hat and blazer and board a bus that stopped right outside clare House, heading to the Folkestone bus station. From there, I would catch another bus to Hythe and the school. With the buses running on time, the journey took just under an hour. And so, I embarked on another phase of my school life. Surprisingly, despite my baldness, I was not harassed by the other boys. In fact, they were quite friendly, and I made good friends with one of them. Attending the lessons was not a chore; quite the opposite. We covered all the usual subjects and even delved into a couple of languages. I learned a lot during my time at this school. I didn't mind the traveling, especially as wearing the colorful uniform often sparked conversations with other passengers on the bus. I suppose I'm a bit of a showman at heart!<br>Life during that time held its own blend of joys and sorrows. While weekdays were spent immersed in a school that captured my heart, weekends offered solace among the few friends I had made at 167 Folkestone Road.<br>However, the shadow of poverty loomed over the streets surrounding clare House, particularly Clarendon Street and Clarendon Place, where terraced houses lined the roads, punctuated only by corner shops and the occasional chippie.<br>My friendships, forged during my time at Belgrave Primary School, provided a sense of connection, even if you didn't always engage in regular play together. Yet, amidst these fleeting moments of camaraderie, a devastating blow struck. Returning home one day during a game of football, I was met by a neighbour who delivered the heart-wrenching news: my father had passed away from a massive heart attack. It was a moment that shattered my world, leaving me with grief and uncertainty. Losing the person I loved most at such a tender age was an unimaginable pain to bear, marking September 1951 as a turning point in my young life. I was told later, that baby Phillip was on my Fathers knee when this awful event took place.<br>Several days following the tragic event, the family gathered in the downstairs lounge to discuss the arrangements for our father's funeral. Among those present, I recall my brother Michael, who had returned home after being invalided out of the navy, adding another blow to our already grieving family. Lionel, dressed in his naval uniform, was there too, alongside David, who was undergoing training at a hotel in Folkestone, a placement arranged by our father. Another notable presence was my step-sister Zena, the mother of Peter, who had been with us at the Horsham boarding school. And, of course, our brave and courageous mother.<br>However, what followed during that discussion has remained etched in my memory, haunting me with unanswered questions to this day. I cannot recall the exact words or actions that triggered it, but Zena became upset with something that I said or did. Without anyone coming to my defense or explaining the situation, she made the painful declaration that I should not attend our father's funeral. The absence of clarity surrounding my exclusion from the funeral has left me grappling with unresolved feelings and a lingering sense of incompleteness regarding my father's passing.<br><br>Life without Dad brought significant challenges, especially for our mother, who not only managed the hotel but also bore the weight of its financial burdens. In the subsequent year, I lost my placement at Manor House School due to the overwhelming cost of tuition. By February 1952, at the age of twelve, I was enrolled in Astor Avenue Secondary Modern School. Over the next three years, life settled into a routine as we navigated the best we could. Michael stepped in to assist Mum with the day-to-day operations of the business, while she received support from Biddy, a kind-hearted lady, and Irene, a young helper. Attending school became a mechanical task for me; though physically present, my mind wandered elsewhere, struggling to find focus. Every lunchtime, I walked home to clare House, where Mum or Biddy would ensure I had a meal. After eating, I bid farewell and retraced my steps back to school a routine I repeated for the duration of my time there. While classmates formed bonds and engaged in games, I remained somewhat isolated, lacking close friends.<br>On weekends, I took on the responsibility of looking after Phillip, often taking him out in his pram for outings. One memorable day, we visited Penchester Park, where a small river flowed toward the seafront. As we sat by the bank enjoying sandwiches prepared by Biddy, a startling sight caught my eye a white bundle floating downstream. Reacting swiftly, I secured the pram and rushed into the water, rescuing a baby as it drew near. We scanned the area upstream, where we spotted an overturned pram; the baby, unstrapped, had tumbled into the river. Moments later, a distressed woman arrived, frantically searching for her child. Seeing the woman I gladly returned the baby to her, who was overcome with relief and gratitude and asked for my name. Then we had to return home, I was soaking wet, will I be believed when I tell what had happened?<br><br>Another significant event for the family was Michael marrying Irene, a natural progression given their close working relationship. Irene was a lovely young woman, while Michael was both intelligent and handsome, having earned accolades for his academic achievements, including passing exams with merits. Despite being on a path that could have led him to university, he chose to join the Royal Navy.<br>I remember a particular moment when we were both in the lower lounge, Michael studying for a customs exam while we listened to classical music. Suddenly, Michael began shaking uncontrollably, experiencing convulsions. I rushed to his side, feeling utterly helpless. Thankfully, Mum heard my panicked shouts and rushed to our aid. She guided Michael to the floor, directing me to fetch a spoon from the cutlery drawer. Placing the spoon in his mouth, she prevented him from biting his tongue until the episode passed, and Michael could rest.<br>Confused and concerned, I asked Mum what had happened. It was then that she revealed the reason for Michael's departure from the Navy: he was epileptic. He had experienced similar episodes in his youth, and while doctors had suggested he might outgrow them, the incident on board his ship proved otherwise.<br>Lionel continued to thrive in his naval career, achieving the rank of petty officer, though the specifics of his duties remained a mystery to us. The last time we saw him was at Michael's wedding, where he mentioned his upcoming assignment on the aircraft carrier HMS Centaur. There's one remarkable moment I must mention about Lionel: he was selected as one of the sailors to pull the gun carriage carrying King George during his funeral parade in London.<br>Meanwhile, David decided to leave his position at the Burlington Hotel in Folkestone as the summer season approached in Dover, signaling the start of the cross-channel ferry operations. He joined one of these ships, effectively becoming a part of the Merchant Navy.<br>When you work on these vessels, you sign articles for the duration of the voyage and receive a discharge book, akin to a passport, with your photo and relevant details. Upon completing your term, the book is stamped again, indicating your rating. In David's case, his rating was Asst Stwd (Assistant Steward). This book could serve as a portfolio for future employment opportunities with other companies.<br>With Micheal married Lionel and David occupied with their careers, I found myself as the only one left who could offer assistance to my mother. Of course, Phillip was there, but he was still too young to fully understand the situation.<br><br>One day, I encountered a lady who lived a few doors away from clare House, Mrs. Cotton. I believed she was an acquaintance of my mother. As I was entering my teens, I found her quite attractive for her age, being a widow. Mrs. Cotton mentioned to me that she owned a Fruit &amp; Vegetable shop on Dover's Tower Street and was in need of someone to handle deliveries on Saturday mornings and occasionally on Wednesday afternoons. Without hesitation, I eagerly accepted the offer, thrilled at the prospect of my first part-time job that would provide me with my own pocket money to spend however I pleased.<br>Dover boasted four cinemas in total. The Odeon, situated atop the town, was the most prestigious, albeit not easily accessible. Despite the challenge, it was considered the best in Dover, with an organ that played enchanting music before each film screening. Decked out in ornate decor from the 1930s, a visit to the Odeon promised an enjoyable experience with a unique ambience.<br>The Gaumont cinema, located in midtown, was a more modern establishment, offering comfortable seating and continuous movie screenings throughout the week. This was the cinema I frequented most often, as it was conveniently situated for me. I recall one memorable evening when I took my heavily pregnant mother, a fan of one of the film stars, to a screening. As we exited the auditorium, I had to intervene when she inadvertently linked arms with a bewildered stranger, jokingly I said to her "come on Mum you have enough men in her life already, let that poor man go ".<br>Another cinema I frequented was the Plaza, a little further down from the Gaumont. Although it was nicknamed 'The Flea Pit' due to its affordability, I always enjoyed my time there. One film that left a lasting impression on me was 'Carmen' starring Dorothy Dandridge; I was so captivated by the music and singing that I watched it three times. Lastly, there was the ABC Grenada, just off the market square. As a child, I was allowed to attend the Saturday morning screenings, which were tailored for young children like myself. This early introduction to cinema became a regular part of my routine, especially in my early teens, now that I had a part-time job."<br>I must have watched nearly every movie featuring Humphrey Bogart, James Cagney, George Raft, Lon Chaney, Peter Lorre, Clarke Gable, John Wayne, and the list goes on. Each film left its mark on me, not necessarily for the violence, which by today's standards was relatively mild, but for the compelling stories they told.<br>In my late teens, I witnessed the birth of rock &amp; roll music, which became widely available. I fondly recall attending Saturday night dances at the town hall and the Co-op hall, where I had the privilege of seeing live performances by Lonnie Donegan and Bill Haley and His Comets. Then came the emergence of coffee shops with jukeboxes. I vividly remember one evening, dressed in my best attire, I strolled down to the market square where a new coffee shop had opened its doors. As I approached, the vibrant sounds of rock &amp; roll spilled onto the street, drawing me in. However, in my eagerness, I failed to notice the clear glass front door and embarrassingly walked right into it, becoming unintentional entertainment for those inside. Despite the embarrassment, I quickly gathered myself and turned away, never returning to that coffee shop again.<br>In those years, there were gangs of youths known as Teddy Boys, clad in long jackets and drainpipe trousers, with thick crepe-soled shoes often referred to as 'beetle crushers.' Most of these boys sported a hairstyle slicked back into what they called a 'Ducks Arse.' Whenever I caught sight of them, I swiftly retreated to avoid their notice. Another group that emerged during that era were the Mods, distinguished by their clean-cut appearance, tight-fitting suits, and pointed shoes known as 'winkle pickers.' Their preferred mode of transportation was the Vespa scooter. I always steered clear of these subcultures, preferring to remain a loner rather than aligning myself with any particular group.</p>
        </div>
     
        
        <a href="/chapters/chapter/chapter3/" class="btn btn-secondary">Previous Chapter</a>
    
    
        <a href="/chapters/chapter/chapter5/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MyStory</title>
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">

    <!-- ✅ Google Fonts & W3.CSS -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="/static/css/main.css">


    <!-- ✅ Lightbox2 CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">

    <!-- ✅ Load TinyMCE v7 (Only One Instance with API Key) -->
    <script src="https://cdn.tiny.cloud/1/h1jz6d9xttu6bz1hsi7nyginwsxowh8nusj41k6bl6qj9o7z/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

    <!-- ✅ Lightbox2 JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js"></script>
</head>


<body class="w3-light-grey">

    <!-- Header Section -->
    <header class="site-header w3-blue-grey">
        <h1 class="title">The Story of an Ordinary Man with an Extra-ordinary Life</h1>
        <img src="/static/images/P%20in%20Positano.jpg" alt="Header Image" class="header-image">
        <h2 class="subtitle">Through the simplicity of my existence, I unearthed the profound truth <br> that to love and to be loved is the greatest adventure of all...</h2>
    </header>

    

   <!-- Navigation -->
<div class="w3-bar w3-blue-grey w3-padding">
    
    <a href="/chapters/login/" class="w3-button w3-blue w3-round w3-right">Login</a>
    
    <a href="/" class="w3-bar-item w3-margin-left w3-button w3-round-large w3-cyan">Home</a>
    <a href="/chapters/chapter/new/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-teal">New Chapter</a>
    <a href="/chapters/gallery/" class="w3-bar-item w3-button w3-round-large w3-margin-left w3-yellow">Photo-Gallery</a>
    
    
</div>


    <!-- Page Content -->
    <div class="w3-container w3-padding content-container w3-blue-grey w3-round-large w3-margin-top">
        
    <a href="/chapters/chapter/chapter5/edit/" class="btn btn-primary mt-3">Edit Chapter</a> |
    <a href="/" class="btn btn-primary mt-3">Back to All Chapters</a>
    <hr class="w3-border-top color-green">
    <div class="w3-display-container" style="position: relative; width: 100%; height: 400px; background-color: #ccc;">
        
            <img src="/media/images/claireHouse.jpg" alt="Cover Image" class="w3-image w3-round"
                 style="width: 100%; height: 100%; object-fit: cover;">
        
    <hr class="w3-border-top color-green">
        <div class="w3-display-middle">
            <h1 style="color: white !important; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">
                Chapter 5
            </h1>
        </div>
    </div>
  <hr class="w3-border-top color-green">
    <div class="chapter-detail">
        
            <h2><h3 class="subtitle-section"><strong>Clare House</strong>-Life's twists and turns often unfold swiftly, leaving us with little control over the course of events .</h3></h2>
        
 <hr>       
        <div class="content">
            <p>After<a href="../../../media/images/wedding.jpg" target="_blank" rel="noopener">&nbsp;Micheal &amp; Irene</a><a href="../../../static/images/wedding.jpg">&nbsp;</a>were married, they stayed on at Clare House for a few more months until they found somewhere to live, and then they moved out. Biddy continued to be a great help to my mother, providing much-needed support during a challenging time.<br>Then, one day, a new person arrived at Clare House. He was introduced to me as Eddie, the brother of one of my uncles, although I wasn't aware of our family connection at the time. Little did I know that he was soon going to become my stepfather, bringing significant changes to our lives. At that time, I lacked the business acumen and knowledge required to run a business, and I could sense that my mother must have been feeling overwhelmed, both emotionally and financially, since the loss of Dad.<br>Eddie's arrival seemed to offer a glimmer of hope and stability, and before long, he and my mother were married. As for us boys, Phillip and I were too young to fully comprehend the implications of the marriage. Meanwhile, Micheal, Lionel, and David were preoccupied with their own lives and responsibilities.<br>In the initial months following Eddie's arrival, things felt somewhat awkward. I wasn't sure what to say or how to interact, so I stuck to my usual routine. Each morning, around 7 o'clock, I'd make a trip to the local bakery, conveniently located just across the road in an area known as Winchelsea Rd. The bakery, nestled into the side of a hill, was a fascinating sight for a young boy like me. Stepping inside, I'd be greeted by the aroma of freshly baked bread and the sight of large mixers and ovens. Eagerly, I'd collect our order and hurry back home to clare House, enjoying the taste of a fresh crusty roll along the way.<br>This routine repeated itself three days a week, depending on how busy clare House was. Upon my return, Eddie would often be up and about, preparing tea for Mum and himself. We'd exchange greetings, and then I'd settle down to have some breakfast before heading off to school. The routine became familiar, and we all adjusted to our new dynamic.<br>However, our lives were soon to undergo another significant change with the news of Mum's pregnancy. Over the next three years, she brought four more children into the world: Tony, Carol, and twins Steven and Paul. While this undoubtedly brought joy and fulfillment to Eddie, for me, Phillip, and perhaps even Mum, it introduced a new set of challenges and adjustments. The dynamics of our family shifted once again, as we navigated the complexities of welcoming new siblings and adjusting to our evolving family structure<br>In time as Tony grew he joined Phillip and myself on our outings where would go for an outing the beach and spend a couple hours there. Tony would be in the push chair and I would Phillip walking beside some time I let him stand on the side of the push so he could ride giving him a rest times.<br>This particular day we were watching men working on some sea defenses it was all fenced off with wire fencing and we stood there on the outside of the fence and watched them going about there work. At the site there was a crane well inside of the fenced site it was what it looked to me anyway the crane started up and was manoeuvring into position when the iron hook on the end of the line swung round over the wire fence onto our side and whacked Phillip on the side of his head, it happened all to quickly to do anything to get out of the way.<br>The workmen stood in horror seeing just what had happened some of them rushed around to give some assistance. The side of Phillips head became a terrible sight enlarged and blue looking. The foreman I presumed he was the foreman got hold of Phillip and rushed him to the hospital. leaving me and Tony in a state of distress.<br>However one of the workmen got us into vehicle and drove us to the hospital where Phillip was it was good that the foreman got Phillip to the hospital quickly where placed ice packs on to bring swelling down they X rayed him, all was good no damage.<br>To this day I still have dreams about it, how Phillip looked with a big blue swelling on the side of his face. Of course I was interrogated by Mum as to how this could of happened. It was a few weeks before we could all get over it. Which Phillip did with no after effects.<br>As Tony grew older, it became increasingly evident that he faced challenges with normal childhood tasks. It became apparent that he would require special needs support as he continued to grow. Meanwhile, Carol blossomed into a lovely little girl, eager to assist our mother and Tony to the best of her abilities. However, managing the twins proved to be quite a handful.<br>Occasionally, guests would stay at clare House, requiring full board accommodation with breakfast, lunch, and dinner provided. Our mother, as always, was the mainstay in the kitchen. When Dad was alive, meal preparation was a collaborative effort between them, often turning into a friendly competition to see who could create the tastiest dish. Of course, Mum emerged victorious every time, but it added a fun element to the tasks.<br><br>However, after Dad's passing, it became evident that Eddie lacked culinary skills. Even serving the meals proved to be a challenge for him, as he had spent most of his life as a seaman and had little experience in the kitchen.<br>With Mum's pregnancy, there were times when she couldn't be in the kitchen at all. Recognizing this, Mum began teaching me some simple recipes that I could prepare during her absences to help manage the cooking duties. I did have Biddy around at times to assist me<br>Returning to the present, it was clear that Eddie lacked culinary skills. Despite his years spent at sea as a seaman, cooking and serving meals were foreign tasks to him. Nonetheless, he had to adapt and do his best to contribute to the household.<br>Unbeknown to me, this experience laid the foundation for a future career in hospitality. Academic pursuits held little appeal for me, especially as I witnessed the challenges at home.<br>It seemed that Eddie was grappling with alcoholism, likely exacerbated by the pressures of managing clare House. Despite this, he still had responsibilities beyond the business, with four children needing his attention.<br>Eddie often requested that I fetch him a bottle of gin from the pub or off-license, a task I used to fulfill without question. However, as his drinking habits became more apparent, I began to avoid his requests, preferring not to be around when he asked.<br><br>When my brothers learned about what was happening, they banded together to support our mother and attempted to remove Eddie from the picture. However, Mum adamantly refused to entertain the idea. As for me, I was in no position to take any action, so the matter was eventually set aside, and we continued with our lives.<br><br>The children were growing rapidly, with Carol increasingly assisting Mum. Tony received aid for his disabilities, while the twins continued to be a handful, lacking the firm guidance they needed from their father. Though I earned some respect from them, I didn't interact with them much. Phillip, on the other hand, spent most days with them.<br><br>In my final year at school, I still had to leave when Religious Education was taught, and instead this year, I attended music lessons. The previous year, it was art with Mr. Beaumont, a nice guy, but I struggled with art. The year before that was woodwork with Mr. Hayward, an elderly gentleman, but that was even more challenging for me. So, music it was for my last year, taught by Mr. Dickinson.<br>It was in this class that I met my best mate &amp; only friend I had made at this school, Sid King. I can't recall why he was in this class, but we bonded instantly, despite coming from different backgrounds - me from Folkestone Road and Sid from Clarendon Road.<br><br>Throughout the year, we were inseparable. After school, we'd often head to the cinema or occasionally take the bus to the Folkestone swimming pool. At some point, we both enrolled in The Big Brother Scheme to immigrate to Australia. Surprisingly, our parents gave us permission, perhaps eager to see us venture out on our own. We even went as far as having chest X-rays, and we both passed. However, after going through all the paperwork and preparations, Sid decided he didn't want to go through with it, and I certainly wasn't going to go alone.<br>Despite that, Sid and I remained great friends until we eventually lost contact when we both left to start our working lives.<br>As my birthday fell in February, I could leave school at the Easter break, which I did. In Dover during that period, the primary employment options were either working on the cross-channel ferries when they resumed for the summer season or in the coalmines, of which there were three not too far from Dover. However, working in the mines was definitely not something I had in mind. Instead, I decided to apply for a job on the cross-channel ferries, which started operating again at Easter. I was hired.</p>
        </div>
     
        
        <a href="/chapters/chapter/chapter-4/" class="btn btn-secondary">Previous Chapter</a>
    
    
        <a href="/chapters/chapter/chapter-6/" class="btn btn-secondary">Next Chapter</a>
    
    </div>

    </div>

    <hr>

    <footer class="w3-container w3-blue-grey w3-padding w3-margin-top w3-center w3-round-large">
        <div class="w3-content" style="max-width: 600px; margin: 0 auto; text-align: center;">
            
            <!-- Author Photo -->
            <img src="/static/images/favicon.ico" alt="Author Photo"
                 class="w3-circle" style="width:80px;height:80px;object-fit:cover;border:2px solid white; margin: 0 auto;">
            
            <!-- Quote -->
            <p class="w3-medium w3-margin-top w3-opacity" style="margin-top: 12px; text-align: center;">
                <em>"Every life holds a story. Mine just happens to be written here."</em>
            </p>
            
            <!-- Decorative Line -->
            <hr style="width:60%; margin: 10px auto; border:1px solid #ccc; opacity:0.3;">
            
            <!-- Signature -->
            <p class="w3-medium w3-opacity" style="text-align: center;">
                <em>Thanks for sticking around — you deserve a medal... or at least a cup of tea,</em>
                <strong>Peter</strong>
            </p>
            
            <!-- Copyright --><a href="/chapters/about/" class="w3-bar-item w3-button">About</a>

            <p class="w3-small" style="margin-top: 10px; text-align: center;">&copy; 2025 EasyAS International</p>
            
        </div>
    </footer>
    
    
    
    
    
        
 
        

    <!-- ✅ W3.CSS JavaScript for Responsive Navigation -->
    <script>
        function toggleNav() {
            var nav = document.getElementById("mySidenav");
            if (nav.style.display === "block") {
                nav.style.display = "none";
            } else {
                nav.style.display = "block";
            }
        }
    </script>
  <!-- ✅ TinyMCE Initialization (Ensures it Loads Correctly) -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof tinymce !== "undefined") {
            tinymce.init({
                selector: 'textarea',
                plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
                automatic_uploads: true
            });
            console.log("✅ TinyMCE v7 initialized successfully.");
        } else {
            console.error("❌ TinyMCE failed to load. Check the API key or script URL.");
        }
    });
</script>

<!-- ✅ Lightbox Initialization for Chapter Images -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.parentElement.hasAttribute("data-lightbox")) {
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });
        console.log("✅ Lightbox applied to images.");
    });

</script>
<!-- Toast Message Container -->
<div id="toast" class="w3-hide w3-green w3-padding w3-round-large w3-animate-opacity" 
     style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
    ✅ Backup download started!
</div>
<!-- Toast Trigger for Backup Button -->
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const backupLink = document.querySelector('a[href$="export_chapters/"]');
        const toast = document.getElementById("toast");

        if (backupLink && toast) {
            backupLink.addEventListener("click", () => {
                toast.classList.remove("w3-hide");
                setTimeout(() => {
                    toast.classList.add("w3-hide");
                }, 3000); // Toast visible for 3 seconds
            });
        }
    });
</script>

</body>
</html>
