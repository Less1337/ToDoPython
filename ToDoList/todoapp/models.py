from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title