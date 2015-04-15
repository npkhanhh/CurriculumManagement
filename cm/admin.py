from django.contrib import admin
import cm.models as m

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'name')


admin.site.register(m.Program, ProgramAdmin)
admin.site.register(m.Major)
admin.site.register(m.Subject)
admin.site.register(m.BlockOfKnowledge)