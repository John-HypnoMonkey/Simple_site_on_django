from django.db import models

# Create your models here


class NewsPost(models.Model):
    pub_date = models.DateField()
    title_text = models.CharField(max_length=200)
    content_text = models.TextField()
