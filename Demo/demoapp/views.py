from django.shortcuts import render
from rest_framework.response import Response
from .serializer import StudetSerializer
from .models import Student
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def student_list(request):
    studen_data = Student.objects.all()
    student_lists = StudetSerializer(studen_data,many=True)
    return Response(student_lists.data)

