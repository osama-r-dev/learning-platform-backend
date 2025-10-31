
from rest_framework import serializers
from .models import Employee, Course, Video, Profile


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'


class videoSerializer(serializers.ModelSerializer):
        model = Video
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
