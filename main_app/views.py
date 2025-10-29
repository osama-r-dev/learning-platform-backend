from django.shortcuts import render
from .models import Employee, Course 
from .serializers import EmployeeSerializer, CourseSerializer, videoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

class EmployeeIndex(APIView):

    def get(self, request):   
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status= status.HTTP_200_OK)
            return response
        
class EmployeeDetail(APIView):
    def put(self, request, emp_Id):
        queryset = get_object_or_404(Employee,id = emp_Id)
        serializer = EmployeeSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, emp_Id):
        queryset = get_object_or_404(Employee,id = emp_Id)
        queryset.delete()
        return Response({"message":"You deleted an employee"},status=status.HTTP_200_OK )
        
class CourseIndex(APIView):
    def get(self, request, emp_Id):
        queryset = Course.objects.filter(employee_id = emp_Id)
        serializer = CourseSerializer(queryset, many = True)
        print(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, emp_Id):
        serializer = CourseSerializer(data = request.data)
        employee = get_object_or_404(Employee, id = emp_Id)
        if serializer.is_valid():
            serializer.save(employee = employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
class CourseDetails(APIView):
    def get(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id)
        serializer = CourseSerializer(queryset, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)    
        
class CourseList(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many = True)
        return Response(serializer.data)
        
class VideoList(APIView):
     def get(self, request, emp_Id, course_Id):
        employee = get_object_or_404(Employee, id = emp_Id)
        course = get_object_or_404(Course, id = course_Id, employee = employee)
        videos = course.videos
        serializer = videoSerializer(videos, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
