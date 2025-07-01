from django.contrib import admin
from django.urls import path,include
from .views import student_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/',include('demoapp.urls'))
    path('get/',student_list,name='student_list')
]
