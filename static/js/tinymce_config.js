tinymce.init({
    selector: 'textarea',  // Targets all <textarea> elements
    plugins: 'link image media code',  // Ensure all plugins exist
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | link image | code', 
    menubar: false,
    height: 400
});
