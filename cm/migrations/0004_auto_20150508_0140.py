# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0003_auto_20150508_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockofknowledge',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='cm.Subject', null=True),
            preserve_default=True,
        ),
    ]
