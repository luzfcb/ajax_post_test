from django.db import models
from django.db.models import F


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
