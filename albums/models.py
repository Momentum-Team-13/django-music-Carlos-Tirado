# from turtle import title
# from xml.dom.minidom import AttributeList
from django.db import models
from django.utils import timezone
# import datetime

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(null=True, blank=True, upload_to="images/") #segundo paso para imagenes





    #to see the album name/tittle on the django administration
    def __str__(self):
        return self.title
