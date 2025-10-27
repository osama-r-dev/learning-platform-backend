from django.urls import path
from .views import EmployeeIndex, CourseIndex
urlpatterns = [
  path('employees/', EmployeeIndex.as_view(), name="employee_index" ),
  path('employees/<int:emp_Id>/courses/', CourseIndex.as_view(), name="course_index" ),
  
]

