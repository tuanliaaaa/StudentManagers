from wsgiref import validate
from django.forms import ValidationError
from rest_framework import serializers
from .studentModels import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    StudentName = serializers.CharField(max_length=255)
    StudentCode = serializers.CharField(max_length=255)
    Scores = serializers.FloatField()
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.StudentName = validated_data.get('StudentName', instance.StudentName)
        instance.StudentCode = validated_data.get('StudentCode', instance.StudentCode)
        instance.Score = validated_data.get('Score', instance.Score)
        instance.save()
        return instance