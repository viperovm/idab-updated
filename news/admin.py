from django.contrib import admin
from django import forms
from django.template.defaultfilters import truncatechars

from .models import Event
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EventAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'is_online')

    def get_title(self, obj):
        return truncatechars(obj.title, 20)

    get_title.short_description = 'Заголовок'


# class NewsAdminForm(forms.ModelForm):
#     body = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = NewsBase
#         fields = '__all__'

# class NewsAdmin(admin.ModelAdmin):
#     form = NewsAdminForm


# admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)