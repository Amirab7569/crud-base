from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
    