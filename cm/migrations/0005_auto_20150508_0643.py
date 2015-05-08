# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0004_auto_20150508_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name_en',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name_vi',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
