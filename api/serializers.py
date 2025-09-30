from rest_framework import  serializers

from employees.models import Employee, EmployeeTask

class EmployeeTaskSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=False)
    class Meta:
        model = EmployeeTask
        fields = ["title", "description", "employee",]

class EmployeeSerializer(serializers.ModelSerializer):
    #tasks = serializers.StringRelatedField(many=True, read_only=True)
    tasks = EmployeeTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = ["employee_name", "age", "role", "tasks",]

