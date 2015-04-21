from django.forms import ModelForm
from django import forms
from cm.models import Program


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['program_id', 'name', 'level', 'type', 'description']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()