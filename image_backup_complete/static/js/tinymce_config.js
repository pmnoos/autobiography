tinymce.init({
    selector: 'textarea',  // Targets all <textarea> elements
    plugins: 'advlist lists link image media code textpattern',  // Added missing plugins
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | link image | code | chapterimage bannerimage grammarCheck', 
    menubar: false,
    height: 400,
    setup: function(editor) {
        // Button for inserting a chapter image
        editor.ui.registry.addButton('chapterimage', {
            text: 'Insert Chapter Image',
            icon: 'image',
            onAction: function () {
                let imageUrl = prompt("Enter image URL (from /media/images/):");
                if (imageUrl) {
                    let html = `<a href="${imageUrl}" data-lightbox="gallery" data-title="Chapter Image">
                                    <img src="${imageUrl}" alt="Chapter Image" style="width: 200px; cursor: pointer;">
                                </a>`;
                    editor.insertContent(html);
                }
            }
        });

        // Button for inserting a banner image
        editor.ui.registry.addButton('bannerimage', {
            text: 'Insert Banner Image',
            icon: 'image',
            onAction: function () {
                let bannerUrl = prompt("Enter banner image URL:");
                if (bannerUrl) {
                    let html = `<img src="${bannerUrl}" alt="Banner Image" style="width: 100%;">`;
                    editor.insertContent(html);
                }
            }
        });

        // Grammar check button
        editor.ui.registry.addButton('grammarCheck', {
            text: 'Check Grammar',
            onAction: function() {
                var text = editor.getContent(); // Get the content from the editor

                // Make an AJAX request to the grammar check view
                fetch('/check-grammar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is sent
                    },
                    body: JSON.stringify({ text: text })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.errors.length > 0) {
                        alert('Grammar errors found:\n' + data.errors.map(error => error.message).join('\n'));
                    } else {
                        alert('No grammar errors found!');
                    }
                });
            }
        });
    }
});
