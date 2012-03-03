__author__ = 'yin'
from django.contrib import admin
from blog import models

admin.site.register(models.Article)
admin.site.register(models.Category)
