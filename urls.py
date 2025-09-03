from django.contrib import admin
from django.urls import path,include
from .views import student_list,create_student,update_student,get_student,delete_student

urlpatterns = [
    path('get/',student_list,name='student_list'),
    path('create/',create_student,name='create_student'),
    path('update/<int:id>/',update_student,name='update_student'),
    path('getstudent/<int:id>',get_student,name='get_student'),
    path('deletstudent/<int:id>',delete_student,name='delete_student')
]
