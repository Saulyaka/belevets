from django.db import models


class PleinAir(models.Model):
    title = models.CharField(max_length=100)
    advt = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField()
    duration = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.FileField(upload_to='pleinair/images', blank=True)

    def __str__(self):
        return self.title
