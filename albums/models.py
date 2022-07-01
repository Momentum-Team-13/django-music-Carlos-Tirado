from turtle import title
from xml.dom.minidom import AttributeList
from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    #to see the album name/tittle on the django administration
    def __str__(self):
        return self.title
