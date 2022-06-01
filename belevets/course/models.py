from django.db.models.deletion import CASCADE
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description_public = models.TextField()
    description_private = models.TextField(blank=True)
    announcement = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.FileField(upload_to='course/images', blank=True)
    video = models.FileField(upload_to='course/video', blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to='course/imges', blank=True)
    text = models.TextField(blank=True)
    materials = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course}, {self.title}"


class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    image = models.FileField(upload_to='course/imges', blank=True)
    video = models.FileField(upload_to='course/video', blank=True)

    def __str__(self):
        return f"{self.title}, {self.section}"
