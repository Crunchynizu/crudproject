from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # List students
    path('student/<int:pk>/', views.student_detail, name='student_detail'),  # View student
    path('student/add/', views.student_create, name='student_create'),  # Add student
    path('student/edit/<int:pk>/', views.student_update, name='student_update'),  # Edit student
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),  # Delete student
]
