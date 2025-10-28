
from rest_framework import serializers
from .models import Employee, Course, Video


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class videoSerializer(serializers.ModelSerializer):
        model = Video
        fields = "__all__"

