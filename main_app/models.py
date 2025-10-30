from django.db import models
from django.conf import settings
# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length= 50)
    department = models.CharField(max_length= 50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='employee')

    def __str__(self):
        return f"{self.name} - {self.department}"
    
    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        super().delete(*args, **kwargs)

class Course(models.Model):
    course_img = models.ImageField(upload_to='course_images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    skills = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, related_name="courses")

class Video(models.Model):
    thumbnail = models.ImageField(upload_to='course_images/', blank=True, null=True)
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length=250)
    skills = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, on_delete= models.CASCADE,related_name='videos')
    video = models.FileField(upload_to='videos/',max_length=300)



class Profile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=250, blank=True)
    contact_email = models.EmailField(blank=True, null=True)