from django.shortcuts import render
from rest_framework.decorators import APIView
from .studentModels import Student
from .studentSerializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from StudentManager.roleLoginDecorater import RoleRequest
from django.db import connection
#-------code kém bảo mật-------
class StudentsByName(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['NormalUser',]))
    def get(self,request,name):
        # cursor=connection.cursor()
        # cursor.execute("Select * from  user_user where user_user.Username like '%%'")
        # a=cursor.fetchall()
        sql="Select * from  student_student where student_student.StudentName like '%%"+name+"%%'"
        print(sql)
        user= Student.objects.raw(sql)
        if not user:
            return Response({"messager":"Không tồn tại học sinh này"},status=status.HTTP_204_NO_CONTENT)
        studentSerializer=StudentSerializer(user,many=True)
        return Response(studentSerializer.data,status=status.HTTP_200_OK)


#-------Code phòng chống tấn coogn bằng sql injection------
# class StudentsByName(APIView):
#     @method_decorator(RoleRequest(allowedRoles=['NormalUser',]))
#     def get(self,request,name):
#         students = Student.objects.filter(StudentName__contains=name)
#         studentsSerializer = StudentSerializer(students,many=True)
#         return Response(studentsSerializer.data,status=status.HTTP_200_OK)