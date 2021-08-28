from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    time = models.DateTimeField(default=timezone.now, verbose_name="زمان")
    desc = models.TextField(verbose_name="توضیحات")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")

    class Meta:
        verbose_name = "نوشته"
        verbose_name_plural = "نوشته ها"

    def __str__(self):
        return self.title