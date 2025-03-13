from django import forms
from .models import Chapter
from tinymce.widgets import TinyMCE

from django import forms
from tinymce.widgets import TinyMCE
from .models import Chapter

class ChapterForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    subtitle = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}), required=False)

    class Meta:
        model = Chapter
        fields = ['title', 'subtitle', 'content']


    class Meta:
        model = Chapter
        fields = ['title', 'subtitle', 'content', 'cover_image']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_class = 'w3-input w3-border w3-round'
        self.fields['title'].widget.attrs.update({'class': input_class})
        self.fields['subtitle'].widget.attrs.update({'class': input_class})
        self.fields['content'].widget.attrs.update({'class': input_class})
        self.fields['cover_image'].widget.attrs.update({'class': input_class})
