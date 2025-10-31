from django.contrib import admin
from .models import Employee, Course, Video, Profile
# Register your models here.
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Profile)