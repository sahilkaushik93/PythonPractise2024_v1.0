from django.db import models

# Create your models here.

# Database model
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        '''This function defines what class instance will return once
           instance is printed using "print" function.
        '''
        return f"{self.first_name} {self.last_name}"