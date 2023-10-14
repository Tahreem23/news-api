from django.db import models

class Article(models.Model):
    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField()
