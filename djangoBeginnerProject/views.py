# render the home.html page from template folder
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
