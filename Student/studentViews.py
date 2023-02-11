from django.shortcuts import render
from rest_framework.decorators import APIView
from .studentModels import Student
from .studentSerializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class StudentsByName(APIView):
    def get(self,request,name):
        students = Student.objects.filter(StudentName__contains=name)
        studentsSerializer = StudentSerializer(students,many=True)
        return Response(studentsSerializer.data,status=status.HTTP_200_OK)