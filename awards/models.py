from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
   instance.profile.save()
# Create your models here.
class Project(models.Model):
    project_image = models.ImageField(upload_to = 'image/')
    project_title = models.TextField()
    project_description = models.TextField()
    project_link = models.TextField()
    post = HTMLField()
    user = models.ForeignKey(User,related_name='project')
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
    profile_photo= models.ImageField(upload_to = 'image/',null=True)
    user = models.OneToOneField(User,related_name='profile' ,on_delete=models.CASCADE,)
    

    def __str__(self):
    
        return self.bio

    def save_profile(self):
        self.save()

   
    @classmethod
    def search_profile(cls, name):
        profile = cls.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = cls.objects.filter(user=id).first()
        return profile

class Ratings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Project,on_delete=models.CASCADE,related_name='likes')
    design = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    creativity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    