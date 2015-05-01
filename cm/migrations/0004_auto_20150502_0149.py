# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0003_auto_20150501_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='self_study_hr',
            field=models.SmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
