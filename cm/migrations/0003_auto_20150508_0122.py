# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0002_auto_20150508_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockofknowledge',
            name='parentId',
            field=models.ForeignKey(null=True, blank=True, to='cm.BlockOfKnowledge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='major',
            name='parentId',
            field=models.ForeignKey(null=True, blank=True, to='cm.Major'),
            preserve_default=True,
        ),
    ]
