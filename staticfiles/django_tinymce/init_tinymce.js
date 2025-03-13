function initTinyMCE(el) {
  if (el.closest('.empty-form') === null) {  // Ignore empty inlines
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
    console.error('tinyMCE is not loaded. Check if TINYMCE_JS_URL is set correctly.');
    return;
  }

  initializeTinyMCE(document);

  if (typeof django !== 'undefined' && typeof django.jQuery !== 'undefined') {
    django.jQuery(document).on('formset:added', function(event, $row) {
      if (event.detail && event.detail.formsetName) {
        initializeTinyMCE(event.target);
      } else {
        initializeTinyMCE($row.get(0));
      }
    });
  }
});
