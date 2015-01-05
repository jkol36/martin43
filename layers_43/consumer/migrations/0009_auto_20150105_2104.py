# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0008_profile_has_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default=None, null=True, upload_to=b'/images/profile_pics', blank=True),
            preserve_default=True,
        ),
    ]
