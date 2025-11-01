
from rest_framework import serializers
from .models import Employee, Course, Video, Profile


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'skills', 'thumbnail', 'video']

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
