from django.db import models


class ChangeloggableMixin(models.Model):
    _original_values = {}

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(ChangeloggableMixin, self).__init__(*args, **kwargs)
        self._original_values = {field.name: getattr(self, field.name) for field in self._meta.fields if
                                 field.name not in ['added', 'changed'] and hasattr(self, field.name)}

    def get_changed_fields(self):
        result = {}
        for name, value in self._original_values.items():
            if value != getattr(self, name):
                temp = {}
                temp[name] = getattr(self, name)
                result.update(temp)
        return result
