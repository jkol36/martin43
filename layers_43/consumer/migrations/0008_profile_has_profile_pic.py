# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0007_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_profile_pic',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
