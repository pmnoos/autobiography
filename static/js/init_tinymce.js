function initTinyMCE(el) {
  if (!el.closest('.empty-form')) {  // Ignore empty inlines
      let mce_conf = JSON.parse(el.dataset.mceConf || '{}');

      const fns = [
          'color_picker_callback',
          'file_browser_callback',
          'file_picker_callback',
          'images_dataimg_filter',
          'images_upload_handler',
          'paste_postprocess',
          'paste_preprocess',
          'setup',
          'urlconverter_callback',
      ];

      fns.forEach((fn_name) => {
          if (mce_conf[fn_name] && typeof window[mce_conf[fn_name]] === 'function') {
              mce_conf[fn_name] = window[mce_conf[fn_name]];
          }
      });

      if (mce_conf.selector && mce_conf.selector.includes('__prefix__')) {
          mce_conf.selector = `#${el.id}`;
      } else if (!('selector' in mce_conf)) {
          mce_conf['target'] = el;
      }

      if (el.dataset.mceGzConf) {
          try {
              tinyMCE_GZ.init(JSON.parse(el.dataset.mceGzConf));
          } catch (e) {
              console.warn("TinyMCE GZ init failed:", e);
          }
      }

      if (!tinyMCE.get(el.id)) {
          tinyMCE.init(mce_conf);
      }
  }
}

function ready(fn) {
  if (document.readyState !== 'loading') {
      fn();
  } else {
      document.addEventListener('DOMContentLoaded', fn);
  }
}

function initializeTinyMCE(element) {
  Array.from(element.querySelectorAll('.tinymce')).forEach(area => initTinyMCE(area));
}

ready(function() {
  if (typeof tinyMCE === 'undefined') {
      console.error('TinyMCE is not loaded. Check if TINYMCE_JS_URL is set correctly.');
      return;
  }

  initializeTinyMCE(document);

  if (typeof django !== 'undefined' && typeof django.jQuery !== 'undefined') {
      django.jQuery(document).on('formset:added', function(event, $row) {
          initializeTinyMCE($row.get(0));
      });
  }

  // Initialize TinyMCE once
  tinymce.init({
      selector: 'textarea',
      plugins: 'link image media code',
      toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | link image | code | grammarCheck',
      extended_valid_elements: 'a[href|data-lightbox],img[src|alt|width|height]',

      setup: function(editor) {
          // Button for inserting a chapter image with lightbox
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

          // Button for grammar check
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
});

// Utility function to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
