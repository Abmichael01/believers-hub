from django.db import models
from django.utils import timezone

class Word(models.Model):
    verse = models.CharField(max_length=150)
    verse_content = models.TextField()
    motivation = models.TextField()
    prayer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.verse

class Visit(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)+" Visits"