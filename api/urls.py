from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students/<int:pk>/', views.studentDetailView, name='student-detail'),
    path('employees/', views.EmployeeView.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('blogs/', views.BlogView.as_view(), name='blogs'),
    path('comments/', views.CommentView.as_view(), name='comments'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
]