from django.db import models

class Category(models.Model):
    """
    Model for video categories.
    - Stores the name of a category.
    - Used to organize and filter videos.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    """
    Model for videos.
    - Stores video metadata such as title, description, and creation date.
    - Handles original video file and multiple resolutions (360p, 480p, 720p, 1080p).
    - Supports optional thumbnail image.
    - Allows assignment to multiple categories.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    video_file = models.FileField(upload_to='videos/original/', null=True, blank=True)

    video_360p = models.FileField(upload_to='videos/360p/', null=True, blank=True)
    video_480p = models.FileField(upload_to='videos/480p/', null=True, blank=True)
    video_720p = models.FileField(upload_to='videos/720p/', null=True, blank=True)
    video_1080p = models.FileField(upload_to='videos/1080p/', null=True, blank=True)

    categories = models.ManyToManyField(Category, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
