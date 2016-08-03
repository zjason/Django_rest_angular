from __future__ import unicode_literals

from django.db import models

def upload_location(instance,filename):
    return "./media/%s/%s" %(instance.id,filename)

# Create your models here.
class houseinfo(models.Model):
    location = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    imagesrc = models.CharField(max_length=1000, default="../media/media/None/Dva.png",null=True, blank=True)
    if image is None:
        hasimage = models.BooleanField(default=False)
    else:
        hasimage = models.BooleanField(default=True)

    def __str__(self):
        return self.location