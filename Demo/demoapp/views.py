from django.shortcuts import render
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def student_list(request):
    studen_data = Student.objects.all()
    student_lists = StudentSerializer(studen_data,many=True)
    return Response(student_lists.data)


@api_view(['POST'])
def create_student(request):
    student_data =StudentSerializer(data=request.data)
    if student_data.is_valid():
        student_data.save()
    return Response(student_data.data)


@api_view(['UPDATE'])
def update_student(request,id):
    student_data = Student.objects.get(id=id)
    student_lists = StudentSerializer(instance=student_data,data=request.data)
    if student_lists.is_valid():
        student_lists.save()
    return Response(student_lists.data)


@api_view(['DELETE'])
def delete_student(request,id):
    student_data = Student.objectts.get(id=id)
    student_data.delete()
    return Response('Student Deleted Successfully')

@api_view(['GET'])
def get_student(request,id):
    student_data = Student.objects.get(id=id)
    student_info = StudentSerializer(student_data)
    return Response(student_info.data)





