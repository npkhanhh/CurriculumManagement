# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockofknowledge',
            name='majors',
            field=models.ManyToManyField(to='cm.Major', null=True, blank=True),
            preserve_default=True,
        ),
    ]
