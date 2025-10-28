from django.urls import path
from .views import EmployeeIndex, CourseIndex, EmployeeDetail, VideoList, CourseList
urlpatterns = [
  path('employees/', EmployeeIndex.as_view(), name="employee_index" ),
  path('employees/<int:emp_Id>/', EmployeeDetail.as_view(), name="employee_detail" ),
  path('employees/<int:emp_Id>/courses/', CourseIndex.as_view(), name="course_index" ),
  path('courses/',CourseList.as_view(), name = "course_list"),
  path('employees/<int:emp_Id>/courses/<int:course_Id>/videos/', VideoList.as_view(), name="video_list")
  
]

