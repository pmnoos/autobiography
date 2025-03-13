from django.contrib import admin
from django.contrib import messages
from tinymce.widgets import TinyMCE
from django import forms
from .models import Chapter

class ChapterAdminForm(forms.ModelForm):
    """Custom form to apply TinyMCE only to subtitle & content"""
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
    subtitle = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}), required=False)

    class Meta:
        model = Chapter
        fields = '__all__'

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    form = ChapterAdminForm  # ✅ Use the custom form

    list_display = ('order', 'title', 'subtitle', 'cover_image', 'created_at')  # ✅ Show order field
    search_fields = ('title', 'subtitle')
    ordering = ('order',)  # ✅ Order chapters by 'order' field, not 'created_at'

    fields = ('order', 'title', 'subtitle', 'content', 'cover_image', 'slug')
    readonly_fields = ('created_at', 'updated_at')

    class Media:
        js = ('js/tinymce-init.js',)  

    def save_model(self, request, obj, form, change):
        """Ensure chapter order is set correctly when saved."""
        if not obj.order or obj.order == 999:  # If no order is set, auto-assign
            last_chapter = Chapter.objects.order_by('-order').first()
            obj.order = (last_chapter.order + 1) if last_chapter else 1  
        super().save_model(request, obj, form, change)
        messages.success(request, "Chapter updated successfully!")  # ✅ Success message
