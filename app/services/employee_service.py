# app/services/employee_service.py
from ..models import Employee

def create_employee(data):
    employee = Employee(
        Name=data['name'],
        Email=data['email'],
        Department=data['department']
    )
    return employee

def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    return employee