# render the home.html page from template folder
from django.shortcuts import render

# import Employee model from employees.models
from employees.models import Employee


def home(request):

    # get employee data from database and return it to the template
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)
