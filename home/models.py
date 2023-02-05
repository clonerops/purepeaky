from django.db import models


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255)
    description = models.TextField()
    subDescription = models.TextField()
    footerTitle = models.TextField()
    backgroundVideo = models.FileField()


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='media')
