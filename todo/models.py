from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    time = models.TimeField(verbose_name="زمان")
    desc = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.title