from django.shortcuts import render
from .models import Employee, Course 
from .serializers import EmployeeSerializer, CourseSerializer, videoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()

# To get all the employees and to add a new employee
class EmployeeIndex(APIView):
    permission_classes = [IsAuthenticated]
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
        
# Getting the details of a specific employee  and deleting an employee(Tested)      
class EmployeeDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = get_object_or_404(Employee,id = request.user.employee.id)
        serializer = EmployeeSerializer(queryset, many = False)
        # if serializer.is_valid():
        #     serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request):
        queryset = get_object_or_404(Employee,id = request.user.employee.id)
        serializer = EmployeeSerializer(queryset,data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request):
        queryset = get_object_or_404(Employee,id = request.user.employee.id)
        queryset.delete()
        return Response({"message":"You deleted an employee"},status=status.HTTP_200_OK )
    


 # Adding a course and getting all courses for a specific employee  (Tested)   
class CourseIndex(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Course.objects.filter( employee = request.user.employee)
        serializer = CourseSerializer(queryset, many = True)
        print(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(employee = request.user.employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

 # Getting the details of a specific course and deleting a course (Tested)       
class CourseDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id)
        serializer = CourseSerializer(queryset, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def put(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id, employee = request.user.employee)
        serializer = CourseSerializer(queryset,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id, employee = request.user.employee)
        queryset.delete()
        return Response({"message":"You deleted an course"},status=status.HTTP_200_OK)    
    

        
class CourseList(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many = True)
        return Response(serializer.data)
        
     
class SignupUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)
        if not username or not password:
            return Response({'error': 'Please Enter your information',
                             }, status=status.HTTP_400_BAD_REQUEST)
        
    
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        ) 

        employee = Employee.objects.create(
    user=user,
    name=request.data.get("name"),
    department=request.data.get("department")
)
        
        return Response({
           'id': user.id,
            'username': user.username,
            'email': user.email,
            'employee_id': employee.id,
            'name': employee.name,
            'department': employee.department
        },status=status.HTTP_201_CREATED)
    

class VideoList(APIView):
     def get(self, request, emp_Id, course_Id):
        employee = get_object_or_404(Employee, id = emp_Id)
        course = get_object_or_404(Course, id = course_Id, employee = employee)
        videos = course.videos
        serializer = videoSerializer(videos, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

