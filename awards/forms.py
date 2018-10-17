from django import forms
from .models import Project,Profile
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        