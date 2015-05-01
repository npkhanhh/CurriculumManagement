# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0002_auto_20150410_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockofknowledge',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='regulation',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
