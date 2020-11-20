from django.db import models
from authentication.models import User, get_deleted_user

class Page(models.Model):
    url = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.url

class Log(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET(get_deleted_user))
    description = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.date_time.isoformat(), self.description)
