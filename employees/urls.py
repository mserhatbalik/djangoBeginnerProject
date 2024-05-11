"""
URL configuration for employees app.
"""
from django.urls import path
from . import views

# URL patterns for employees app
urlpatterns = [
    path('<int:id>/', views.employee_detail, name='employee_detail')
]