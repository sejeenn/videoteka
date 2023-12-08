from django.db import models


def video_directory_path(instance: "Video", filename: str) -> str:
    return f"videos/video_{instance.pk}/{filename}"


def preview_directory_path(instance: "Video", filename: str) -> str:
    return f"images/preview_{instance.pk}/{filename}"


class Video(models.Model):
    class Meta:
        ordering = ["pk", "title", "created_at", "views"]

    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    preview_file = models.ImageField(blank=True, upload_to=preview_directory_path)
    video_file = models.FileField(blank=True, upload_to=video_directory_path)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
