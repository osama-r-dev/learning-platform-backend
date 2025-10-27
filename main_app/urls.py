from django.urls import path
from .views import EmployeeIndex, CourseIndex, EmployeeDetail
urlpatterns = [
  path('employees/', EmployeeIndex.as_view(), name="employee_index" ),
  path('employees/<int:emp_Id>/', EmployeeDetail.as_view(), name="employee_detail" ),
  path('employees/<int:emp_Id>/courses/', CourseIndex.as_view(), name="course_index" ),
  
]

