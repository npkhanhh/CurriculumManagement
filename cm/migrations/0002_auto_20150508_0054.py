# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentmethod',
            name='subject_id',
            field=models.ForeignKey(to='cm.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prerequisitessubject',
            name='prerequisites_subject',
            field=models.ForeignKey(to='cm.Subject', related_name='prerequisites'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prerequisitessubject',
            name='subject_id',
            field=models.ForeignKey(to='cm.Subject', related_name='subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='subject_id',
            field=models.ForeignKey(to='cm.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
