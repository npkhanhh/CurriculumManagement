from django.forms import ModelForm
from cm.models import Program


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['program_id', 'name', 'level', 'type', 'description']
