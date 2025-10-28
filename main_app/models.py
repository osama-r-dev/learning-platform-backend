from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length= 50)
    department = models.CharField(max_length= 50)


    def __str__(self):
        return f"{self.name} - {self.department}"
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    skills = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, related_name="courses")


class Video(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length=250)
    skills = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, on_delete= models.CASCADE,related_name='videos')
    video = models.FileField(upload_to='videos/',max_length=300)
