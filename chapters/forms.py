from django import forms
from .models import Chapter
from tinymce.widgets import TinyMCE

class ChapterForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    subtitle = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}), required=False)

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w3-input w3-border w3-round-large',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w3-input w3-border w3-round-large',
        'placeholder': 'Your Email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'w3-input w3-border w3-round-large',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w3-input w3-border w3-round-large',
        'rows': 5,
        'placeholder': 'Your Message'
    }))
