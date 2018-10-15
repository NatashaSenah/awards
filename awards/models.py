from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Project(models.Model):
    project_image = models.ImageField(upload_to = 'image/')
    project_title = models.TextField()
    project_description = models.TextField()
    project_link = models.TextField()
    post = HTMLField()
    phone_number = models.CharField(max_length = 10)
    @classmethod
    def search_by_title(cls,search_term):
        awards = cls.objects.filter(title__icontains=search_term)
        return awards
    #  def __str__(self):
    #     return self.first_name

    def save_project(self):
        self.save()
class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_photo= models.ImageField()
    

    def __str__(self):
    
        return self.bio

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

    @classmethod
    def search_profile(cls, name):
        profile = cls.objects.filter(user__username__icontains=name)
        return profile


    