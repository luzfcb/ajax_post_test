from django.db.models import F
from django.utils import six
from django.db import models


class UpperCaseModelMixin(object):
    """
    Switch to UpperCase the contents of all Charfields and TextFields a model.
    Only works with save.
    NOT works with update .
    I just did this code probably is not the best approach.
    It would be better to create a trigger directly in the database.
    Not fully tested, please do not use it
    """
    def save(self, *args, **kwargs):
        field_names = [field[0].attname for field in self._meta.get_concrete_fields_with_model() if
                       field[0] and isinstance(field[0], (models.TextField, models.CharField))]

        for field_name in field_names:
            field = getattr(self, field_name)
            if field:
                upper_value = six.text_type(field).upper()
                setattr(self, field_name, upper_value)

        super(UpperCaseModelMixin, self).save(*args, **kwargs)


class Document(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    header = models.TextField()
    content = models.TextField()
    footer = models.TextField()

    save_counter = models.IntegerField(default=1, editable=False)

    is_locked = models.BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        if self.pk:
            self.save_counter = F('save_counter') + 1
        super(Document, self).save(*args, **kwargs)
