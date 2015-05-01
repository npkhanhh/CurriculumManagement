from django.conf.urls import patterns
from django.contrib import admin
from django.http import HttpResponse
import cm.models as m



# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'name')
    pass

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'name_en')
    pass

admin.site.register(m.Program, ProgramAdmin)
admin.site.register(m.Major)
admin.site.register(m.Subject, SubjectAdmin)
admin.site.register(m.BlockOfKnowledge)