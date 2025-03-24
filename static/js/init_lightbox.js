document.addEventListener("DOMContentLoaded", function () {
    if (typeof lightbox !== "undefined" && typeof lightbox.option === "function") {
        lightbox.option({
            resizeDuration: 200,
            wrapAround: true,
            albumLabel: "Image %1 of %2",
            fadeDuration: 300
        });
    } else {
        console.error("Lightbox failed to initialize. Check script import.");
    }
});
