from django.db import models  # Importing models module from django.db

# Defining Employee model which inherits from models.Model
class Employee(models.Model):
    first_name = models.CharField(max_length=100)  # Name field, a character field with maximum length of 100
    last_name = models.CharField(max_length=100)  # Last name field, a character field with maximum length of 100
    photo = models.ImageField(upload_to='photos')  # Photo field, an image field where images will be uploaded to 'images' directory
    designation = models.CharField(max_length=100)  # Designation field, a character field with maximum length of 100
    email = models.EmailField(max_length=100, unique=True)  # Email field, an email field with maximum length of 100, must be unique
    phone_number = models.CharField(max_length=12, blank=True)  # Phone number field, a character field with maximum length of 12, can be blank
    created_at = models.DateTimeField(auto_now_add=True)  # Created at field, a datetime field which is automatically set to the current date and time when the object is first created
    updated_at = models.DateTimeField(auto_now=True)  # Updated at field, a datetime field which is automatically set to the current date and time whenever the object is saved

    # Defining a string representation of the model
    def __str__(self):
        return self.name  # Return the name of the employee