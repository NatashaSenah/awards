from rest_framework import serializers
from .models import Project,Profile

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_image','project_title','project_description','project_link','phone_number','post']   

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'bio','profile_photo','user']   
     
     
    
    