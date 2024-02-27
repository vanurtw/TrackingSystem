from django.contrib.auth import get_user_model
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


ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'


class ChangeLog(models.Model):
    TYPE_ACTION = [
        (ACTION_CREATE, 'создание'),
        (ACTION_DELETE, 'удаление'),
        (ACTION_UPDATE, 'обновление')
    ]
    changed = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    model = models.CharField(max_length=255, verbose_name='tablica', null=True)
    record_id = models.IntegerField(verbose_name='ID zapisi', null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, verbose_name='user')
    action_on_model = models.CharField(choices=TYPE_ACTION, null=True, verbose_name='action')
    data = models.JSONField(default={}, verbose_name='Изменяемые данные', null=True)
    ipaddress = models.CharField(max_length=15, verbose_name='IP address', null=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['changed']

    @classmethod
    def add(cls, instance, user, ipaddress, action_on_model, data, id=None):
        log = ChangeLog.objects.get(id=id) if id else ChangeLog()
        log.model = instance.__class__.__name__
        log.record_id = instance.pk
        if user:
            log.user = user
        log.ipaddress = ipaddress
        log.action_on_model = action_on_model
        log.data = data
        log.save()
        return log.pk
