from django.contrib import admin
from django.urls import path,include
from .views import student_list,create_student

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/',include('demoapp.urls'))
    path('get/',student_list,name='student_list'),
    path('create/',create_student,name='create_student')
]
