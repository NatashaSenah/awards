from django import forms
from .models import Project
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date']
       
        