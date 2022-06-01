from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.FileField(upload_to='blog/images')
    extra_image = models.FileField(upload_to='blog/images', blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Blog, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.article.title
