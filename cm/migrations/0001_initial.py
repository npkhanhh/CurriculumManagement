# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('evidence_assessment', models.TextField()),
                ('criteria', models.TextField()),
                ('level', models.TextField()),
                ('standard_achieved', models.TextField()),
                ('percentage', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlockOfKnowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('num_of_credit', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LearningOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LearningOutcomeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LearningOutcomeHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lo_category', models.ForeignKey(to='cm.LearningOutcomeCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrerequisitesSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('program_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
                ('goal', models.TextField(default='')),
                ('num_of_year', models.IntegerField()),
                ('num_of_credit', models.IntegerField()),
                ('candidates', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('graduation_requirement', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=200)),
                ('type', models.IntegerField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=20, unique=True)),
                ('name_en', models.CharField(max_length=200)),
                ('name_vi', models.CharField(max_length=200)),
                ('num_of_credit', models.SmallIntegerField()),
                ('theory_hr', models.SmallIntegerField()),
                ('practice_hr', models.SmallIntegerField()),
                ('self_study_hr', models.SmallIntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('regulation', models.TextField(null=True, blank=True)),
                ('program_id', models.ForeignKey(to_field='program_id', to='cm.Program')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('goal', models.ForeignKey(to='cm.Goal')),
                ('subject', models.ForeignKey(to='cm.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectLo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField()),
                ('level', models.CharField(max_length=100)),
                ('subject_goal', models.ForeignKey(to='cm.SubjectGoal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('week_no', models.IntegerField()),
                ('title', models.TextField()),
                ('subject', models.ForeignKey(to='cm.Subject')),
                ('teaching_schedule_lo', models.ManyToManyField(to='cm.SubjectLo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teachingmethod',
            name='teaching_schedule_method',
            field=models.ManyToManyField(to='cm.TeachingSchedule'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together=set([('subject_id', 'program_id')]),
        ),
        migrations.AddField(
            model_name='resource',
            name='subject_id',
            field=models.ForeignKey(to_field='subject_id', to='cm.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prerequisitessubject',
            name='prerequisites_subject',
            field=models.ForeignKey(to='cm.Subject', to_field='subject_id', related_name='prerequisites'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prerequisitessubject',
            name='subject_id',
            field=models.ForeignKey(to='cm.Subject', to_field='subject_id', related_name='subject'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='prerequisitessubject',
            unique_together=set([('subject_id', 'prerequisites_subject')]),
        ),
        migrations.AddField(
            model_name='major',
            name='program_id',
            field=models.ForeignKey(to_field='program_id', to='cm.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='learningoutcomecategory',
            name='program_id',
            field=models.ForeignKey(to_field='program_id', to='cm.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='lo_header',
            field=models.ForeignKey(to='cm.LearningOutcomeHeader'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='subject_goal_lo',
            field=models.ManyToManyField(to='cm.SubjectGoal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blockofknowledge',
            name='majors',
            field=models.ManyToManyField(null=True, blank=True, to='cm.Major'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blockofknowledge',
            name='program_id',
            field=models.ForeignKey(to_field='program_id', to='cm.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blockofknowledge',
            name='subjects',
            field=models.ManyToManyField(to='cm.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentmethod',
            name='subject_id',
            field=models.ForeignKey(to_field='subject_id', to='cm.Subject'),
            preserve_default=True,
        ),
    ]
