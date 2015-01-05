# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='project',
            field=models.ForeignKey(related_name='Projects', blank=True, to='consumer.Project', null=True),
            preserve_default=True,
        ),
    ]
