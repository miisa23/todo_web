from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'text', 'created_at', 'updated_at', 'category', 'deadline', 'status']
    list_display_links = ['pk', 'title']
    list_editable = ['deadline', 'status']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.Status, StatusAdmin)