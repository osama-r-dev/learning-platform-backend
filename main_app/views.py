from django.shortcuts import render
from .models import Employee, Course, Profile , Video
from .serializers import EmployeeSerializer, CourseSerializer, VideoSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, SAFE_METHODS, BasePermission
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
        
# Getting the details of a specific employee or deleting an employee(Tested)      
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

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:   
            return True
        return request.user and request.user.is_authenticated

 # Getting the details of a specific course and deleting a course or editiing it (Tested)       
class CourseDetails(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id)
        serializer = CourseSerializer(queryset, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def put(self, request, course_Id):
        try:
         queryset = get_object_or_404(Course, id=course_Id, employee=request.user.employee)
         serializer = CourseSerializer(queryset, data=request.data)
         if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
          return Response({"error": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def delete(self, request, course_Id):
        queryset = get_object_or_404(Course, id = course_Id, employee = request.user.employee)
        queryset.delete()
        return Response({"message":"You deleted an course"},status=status.HTTP_200_OK)    
         
class CourseList(APIView):
    permission_classes = [AllowAny]
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
        if User.objects.filter(username=username).exists():
            return Response({"error": "username in use"}, status=status.HTTP_400_BAD_REQUEST)
    
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
        Profile.objects.create(
            employee=employee,
            avatar = "",
            bio="",
            skills="",)
        # before
        # return Response({
        #    'id': user.id,
        #     'username': user.username,
        #     'email': user.email,
        #     'employee_id': employee.id,
        #     'name': employee.name,
        #     'department': employee.department
        # },status=status.HTTP_201_CREATED)
        return Response({"message":"Account created successfully"},status=status.HTTP_201_CREATED)

class VideoList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, course_Id):
        course = get_object_or_404(Course, id=course_Id)
        videos = course.videos.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, course_Id):
        course = get_object_or_404(Course, id=course_Id)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class VideoDetails(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]  

    def get(self, request, course_Id, video_id):
        video = get_object_or_404(Video, id=video_id, course_id=course_Id)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, course_Id, video_id):
       
        course = get_object_or_404(Course, id=course_Id, employee =request.user.employee)
        video = get_object_or_404(Video, id=video_id, course=course)

        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_Id, video_id):
        course = get_object_or_404(Course, id=course_Id,employee =request.user.employee)
        video = get_object_or_404(Video, id=video_id, course=course)
        video.delete()
        return Response({"message": "Video deleted successfully."}, status=status.HTTP_204_NO_CONTENT)    

# To get all of the profiles list in the system
class ProfilesList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        queryset = Profile.objects.all() 
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
        
# To get the details of a specific profile 
class ProfileDetails(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, profile_Id):
        profile = get_object_or_404(Profile, id=profile_Id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

# To get the details of authenticated employee 
class MyProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
      try:
        profile = get_object_or_404(Profile, employee=request.user.employee)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
      except:
          pass

    def put(self, request):
        profile = get_object_or_404(Profile, employee=request.user.employee)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    