from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=12)
    def __unicode__(self):
        return self.name
    class Admin:
        pass

class Article(models.Model):
    title = models.CharField(max_length=64)
    published_at = models.DateTimeField('Data Published')
    content = models.TextField()
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.title
    class Admin:
        pass

class Comment(models.Model):
    content = models.TextField()
    parentId = models.IntegerField()
    article = models.ForeignKey(Article)
    class Admin:
        pass

class Short(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    article = models.ForeignKey(Article)
