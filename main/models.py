from django.db import models

class Page(models.Model):
    url = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.url
