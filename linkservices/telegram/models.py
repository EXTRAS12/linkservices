from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
