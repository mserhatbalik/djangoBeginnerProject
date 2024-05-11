from django.shortcuts import render, get_object_or_404
from .models import Employee

def employee_detail(request, id):
    # Get the employee object with the given pk. If it doesn't exist, return a 404 error.
    employee = get_object_or_404(Employee, id=id)

    # Pass the employee object to the template.
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)