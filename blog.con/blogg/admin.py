from django.contrib import admin
from . models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('status',)
    search_fields = ('title',)

