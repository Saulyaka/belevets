from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone

from blog.models import Blog, Comment
from course.models import Course


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    likes = models.ManyToManyField(Blog)
    comment = models.ManyToManyField(Comment)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=CASCADE)
    courses = models.ManyToManyField(Course)
    payment = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
