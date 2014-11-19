# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('success', models.BooleanField(default=False)),
                ('external_id', models.CharField(max_length=255, null=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('zipcode', models.CharField(max_length=255, null=True)),
                ('product_type', models.CharField(max_length=255, null=True)),
                ('order_quantity', models.IntegerField(default=0)),
                ('materials', models.CharField(max_length=255, null=True)),
                ('deadline', models.DateField()),
                ('description', models.CharField(max_length=255, null=True)),
                ('budget', models.DecimalField(max_digits=10, decimal_places=2)),
                ('is_submitted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_type', models.CharField(max_length=6, choices=[(b'searching', b'Finding a designer'), (b'designer_found', b'Proposed designer'), (b'message_from', b'Message From'), (b'message_to', b'Message To'), (b'designer_accepted', b'Designer selected'), (b'deposit', b'Awaiting Deposit'), (b'inspiration_board', b'Inspiration Board'), (b'proposal', b'Proposal from designer'), (b'change_request', b'Change request'), (b'picture', b'Picture'), (b'final_payment', b'Final Payment'), (b'receipt', b'Order receipt'), (b'status', b'Order status')])),
                ('message', models.CharField(max_length=255, null=True)),
                ('amount_required', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('current_status', models.CharField(max_length=255, null=True)),
                ('project', models.ForeignKey(related_name='updates', to='consumer.Project', null=True)),
                ('user', models.ForeignKey(related_name='updates', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectUpdateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', sorl.thumbnail.fields.ImageField(default=False, null=True, upload_to=b'images/project_pics', blank=True)),
                ('update', models.ForeignKey(related_name='items', to='consumer.ProjectUpdate', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='project',
            field=models.ForeignKey(related_name='payments', to='consumer.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='update',
            field=models.ForeignKey(related_name='pmts', to='consumer.ProjectUpdate', null=True),
            preserve_default=True,
        ),
    ]
