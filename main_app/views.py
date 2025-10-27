from django.shortcuts import render
from .models import Employee, Course
from .serializers import EmployeeSerializer, CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        
class CourseIndex(APIView):
    def get(self, request, emp_Id):
        queryset = Course.objects.filter(employee_id = emp_Id)
        serializer = CourseSerializer(queryset, many = True)
        print(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
            