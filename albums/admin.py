from django.contrib import admin
from .models import Album
from django.conf.urls.static import static

# Register your models here.
admin.site.register(Album)