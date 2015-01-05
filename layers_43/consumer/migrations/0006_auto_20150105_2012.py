# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consumer', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='designer',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='shipping',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
