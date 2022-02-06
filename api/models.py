from django.db import models

# Create your models here.
class Meme(models.Model):
    slugid = models.SlugField() 
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()