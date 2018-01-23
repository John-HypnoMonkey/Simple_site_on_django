from django.db import models

# Create your models here.


class DownloadableFile(models.Model):
    pub_date = models.DateField()
    title_text = models.CharField(max_length=300)
    info_text = models.TextField(default=" ", blank=True)
    file_to_download = models.FileField(upload_to='')
