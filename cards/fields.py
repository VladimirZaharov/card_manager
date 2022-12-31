from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class CardNumberField(models.CharField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(CardNumberField, self).__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        if getattr(instance, self.attname) is None:
            try:
                qs = self.model.objects.filter()
                if self.for_fields:
                    query = {field: getattr(instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                last_item = qs.latest(self.attname)
                value = int(last_item.vendor) + 1
                value = str(value)
                value = str.rjust(value, 7, '0')
            except ObjectDoesNotExist:
                value = ''
            setattr(instance, self.attname, value)
            return value
        else:
            return super(CardNumberField, self).pre_save(instance, add)
