from django.db import models


# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=120, verbose_name='URL слаг')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'


