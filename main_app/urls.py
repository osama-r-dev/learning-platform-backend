from django.urls import path
from .views import EmployeeIndex, CourseIndex, EmployeeDetail, VideoList, CourseList, CourseDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
  path('employees/', EmployeeIndex.as_view(), name="employee_index" ),
  path('employees/<int:emp_Id>/', EmployeeDetail.as_view(), name="employee_detail" ),
  path('employees/<int:emp_Id>/courses/', CourseIndex.as_view(), name="course_index" ),
  path('courses/',CourseList.as_view(), name = "course_list"),
  path('employees/<int:emp_Id>/courses/<int:course_Id>/videos/', VideoList.as_view(), name="video_list"),
  path('courses/<int:course_Id>/', CourseDetails.as_view(), name="course_details"),
  path('login/', TokenObtainPairView.as_view(),name='login'),
  path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh')
]

