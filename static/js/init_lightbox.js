document.addEventListener("DOMContentLoaded", function () {
    console.log("Lightbox script loaded.");

    function initializeLightbox() {
        if (typeof lightbox === "undefined") {
            console.error("Lightbox is not defined. Make sure the script is loaded correctly.");
            return;
        }

        console.log("Initializing Lightbox...");

        // Set Lightbox options
        lightbox.option({
            resizeDuration: 200,
            wrapAround: true,
            albumLabel: "Image %1 of %2",
            fadeDuration: 300
        });

        console.log("Lightbox initialized.");

        // Ensure all images inside chapters have Lightbox applied
        document.querySelectorAll(".chapter-content img").forEach(img => {
            if (!img.closest("a[data-lightbox]")) {  // Avoid re-wrapping already linked images
                let link = document.createElement("a");
                link.href = img.src;
                link.setAttribute("data-lightbox", "gallery");
                link.setAttribute("data-title", img.alt || "Chapter Image");  // Set caption if available

                img.parentNode.insertBefore(link, img);
                link.appendChild(img);
            }
        });

        console.log("Images wrapped with Lightbox links.");
    }

    // Wait a bit to ensure Lightbox is fully loaded
    setTimeout(initializeLightbox, 500);
});
