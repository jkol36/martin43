# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectupdate',
            name='name',
            field=models.CharField(default=None, max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
