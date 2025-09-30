from rest_framework import viewsets
from .serializers import EmployeeSerializer, EmployeeTaskSerializer
from employees.models import Employee, EmployeeTask

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.prefetch_related("tasks")
    serializer_class = EmployeeSerializer

class EmployeeTaskViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTask.objects.prefetch_related("employee")
    serializer_class = EmployeeTaskSerializer
