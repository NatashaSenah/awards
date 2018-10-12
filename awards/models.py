from django.db import models

# Create your models here.
class Project(models.Model):
    project_image = models.ImageField(upload_to = 'image/')
    project_title = models.TextField()
    project_description = models.TextField()
    project_link = models.TextField()
class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
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


    