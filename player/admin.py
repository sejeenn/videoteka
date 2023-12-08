from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "created_at", "video_file", "preview_file"
    list_display_links = "pk", "title", "created_at", "video_file", "preview_file"

