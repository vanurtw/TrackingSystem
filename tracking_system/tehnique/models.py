from django.db import models
from system_track.models import Building
from django.db.models.signals import post_delete, post_save
from system_track.mixins import ChangeloggableMixin
from system_track.signals import journal_save_handler, journal_delete_handler


# Create your models here.


class Tehnique(ChangeloggableMixin, models.Model):
    CHOICES = [
        ('A', 'Техника находится в здании'),
        ('B', 'Техника передана из здания в здание, и ожидает фактического приема'),
        ('C', 'Техника принята в здании')
    ]
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    inventory_number = models.CharField(max_length=255, unique=True, verbose_name='Инвентарный номер')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='tehniques', blank=True, null=True,
                                 verbose_name='Здание')
    parent_building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='parent_tichnique', blank=True,
                                        null=True, verbose_name='Откуда пришло')
    status = models.CharField(max_length=10, choices=CHOICES, default='A', verbose_name='Статус')
    date_crete = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return f'{self.name}'


post_save.connect(journal_save_handler, sender=Tehnique)
post_delete.connect(journal_delete_handler, sender=Tehnique)
