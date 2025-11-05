from django.urls import path
from .views import EmployeeIndex, CourseIndex, EmployeeDetail, VideoList, CourseList, CourseDetails, SignupUserView ,ProfileDetails, ProfilesList, MyProfile, VideoDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
  # add a new employee or get all employees in the system
  path('employees/', EmployeeIndex.as_view(), name="employee_index" ),
  # to get the details or update it or delete a specific employe
  path('employee/', EmployeeDetail.as_view(), name="employee_detail" ),

  # list all courses in the app
  path('allcourses/',CourseList.as_view(), name = "course_list"),
  # add a course or get all courses for a speicific employee
  path('courses/',CourseIndex.as_view(), name = "course_index"),
  # get course's details, update it, or delete a course
  path('courses/<int:course_Id>/', CourseDetails.as_view(), name="course_details"),
    


  path('allprofiles/', ProfilesList.as_view(), name = 'profile_index'),
  path('profiles/<int:profile_Id>/', ProfileDetails.as_view(), name = 'profile_details'),
  path('myprofile/', MyProfile.as_view(), name = 'profile_details'),


  path('courses/<int:course_Id>/myvideos/', VideoList.as_view(), name = 'video_list'),
  path('courses/<int:course_Id>/myvideos/<int:video_id>/', VideoDetails.as_view(), name = 'video_detail'),



  path('login/', TokenObtainPairView.as_view(),name='login'),
  path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
  path('signup/',SignupUserView.as_view(), name = 'signup'),

]

