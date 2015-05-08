from django.db import models

from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Program(models.Model):
    program_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    goal = models.TextField(default='')
    num_of_year = models.IntegerField()
    num_of_credit = models.IntegerField()
    candidates = models.TextField(default='')
    description = models.TextField(default='')
    graduation_requirement = models.TextField(default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    #class Meta:
    #    permissions = (
    #            ("add_program", "Can add new program"),
    #            ("change_task_status", "Can change the status of tasks"),
    #            ("close_task", "Can remove a task by setting its status as closed"),
    #        )

@python_2_unicode_compatible
class Major(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    program_id = models.ForeignKey(Program, to_field='program_id')
    parentId = models.ForeignKey("Major", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Subject(models.Model):
    subject_id = models.CharField(max_length=20)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_vi = models.CharField(max_length=200, null=True, blank=True)
    num_of_credit = models.SmallIntegerField()
    theory_hr = models.SmallIntegerField()
    practice_hr = models.SmallIntegerField()
    self_study_hr = models.SmallIntegerField(null=True, blank=True)
    program_id = models.ForeignKey(Program, to_field='program_id')
    description = models.TextField(null=True, blank=True)
    regulation = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('subject_id', 'program_id'),)

    def __unicode__(self):
        return self.name_en

    def __str__(self):
        return self.subject_id

@python_2_unicode_compatible
class PrerequisitesSubject(models.Model):
    subject_id = models.ForeignKey(Subject, related_name='subject')
    prerequisites_subject = models.ForeignKey(Subject, related_name='prerequisites')

    class Meta:
        unique_together = (('subject_id', 'prerequisites_subject'),)

    def __unicode__(self):
        return self.subject_id

@python_2_unicode_compatible
class Resource(models.Model):
    resource_name = models.CharField(max_length=200)
    type = models.IntegerField(max_length=200)
    subject_id = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.resource_name

    def __str__(self):
        return self.resource_name


@python_2_unicode_compatible
class AssessmentMethod(models.Model):
    subject_id = models.ForeignKey(Subject)
    evidence_assessment = models.TextField()
    criteria = models.TextField()
    level = models.TextField()
    standard_achieved = models.TextField()
    percentage = models.FloatField()

@python_2_unicode_compatible
class BlockOfKnowledge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    num_of_credit = models.SmallIntegerField()
    program_id = models.ForeignKey(Program, to_field='program_id')
    majors = models.ManyToManyField(Major, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    parentId = models.ForeignKey("BlockOfKnowledge", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class LearningOutcomeCategory(models.Model):
    name = models.CharField(max_length=200)
    program_id = models.ForeignKey(Program, to_field='program_id')

    def __unicode__(self):
        return self.name

@python_2_unicode_compatible
class LearningOutcomeHeader(models.Model):
    name = models.CharField(max_length=200)
    lo_category = models.ForeignKey(LearningOutcomeCategory)

    def __unicode__(self):
        return self.name

@python_2_unicode_compatible
class Goal(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.type

class SubjectGoal(models.Model):
    subject = models.ForeignKey(Subject)
    goal = models.ForeignKey(Goal)

@python_2_unicode_compatible
class LearningOutcome(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lo_header = models.ForeignKey(LearningOutcomeHeader)
    subject_goal_lo = models.ManyToManyField(SubjectGoal)

    def __unicode__(self):
        return self.name

class SubjectLo(models.Model):
    description = models.TextField()
    level = models.CharField(max_length=100)
    subject_goal = models.ForeignKey(SubjectGoal)

class TeachingSchedule(models.Model):
    subject = models.ForeignKey(Subject)
    week_no = models.IntegerField()
    title = models.TextField()
    teaching_schedule_lo = models.ManyToManyField(SubjectLo)

class TeachingMethod(models.Model):
    description = models.TextField()
    status = models.SmallIntegerField()
    teaching_schedule_method = models.ManyToManyField(TeachingSchedule)


