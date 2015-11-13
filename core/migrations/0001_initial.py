# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('header', models.TextField()),
                ('content', models.TextField()),
                ('footer', models.TextField()),
                ('save_counter', models.IntegerField(default=0, editable=False)),
                ('is_locked', models.BooleanField(default=False, editable=False)),
            ],
        ),
    ]
