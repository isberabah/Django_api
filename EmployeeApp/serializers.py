from django.db.models.base import Model
from django.db.models.fields import Field
from rest_framework import fields, serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Departments
        fields=('DepartmentId','DepartmentName')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')


