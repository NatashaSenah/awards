from django import forms
from .models import Project,Profile
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date','editor']
        fields = [ 'project_image', 'project_title','project_description','project_link','post','phone_number']
       
   
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


rating_choices = [ 
    (1, '1'), 
    (2, '2'), 
    (3, '3'), 
    (4, '4'), 
    (5, '5'), 
    (6, '6'), 
    (7, '7'), 
    (8, '8'),
    (9, '9'), 
    (10, '10'),
]
class Votes(forms.Form):
    design = forms.CharField(label='Design level', widget=forms.RadioSelect(choices=rating_choices))

    usability = forms.CharField(label='Usability level', widget=forms.RadioSelect(choices=rating_choices))

    creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect(choices=rating_choices))

    content = forms.CharField(label='Content level', widget=forms.RadioSelect(choices=rating_choices))
