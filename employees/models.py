from django.db import models

class Employee(models.Model):
    """Employee models"""
    emp_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name

class EmployeeTask(models.Model):
    """Employee Task model"""
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="tasks"
    )
    date_assigned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.employee.employee_name}"