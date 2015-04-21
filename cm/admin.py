from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import cm.models as m

class SubjectResource(resources.ModelResource):

     class Meta:
        model = m.Subject


# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'name')
    pass

class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource
    pass

admin.site.register(m.Program, ProgramAdmin)
admin.site.register(m.Major)
admin.site.register(m.Subject, SubjectAdmin)
admin.site.register(m.BlockOfKnowledge)