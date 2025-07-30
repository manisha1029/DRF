from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students/<int:pk>/', views.studentDetailView, name='student-detail'),
    path('employees/', views.Employees.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
]