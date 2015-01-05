# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_auto_20150105_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=b'/images/profile_pics', blank=True),
            preserve_default=True,
        ),
    ]
