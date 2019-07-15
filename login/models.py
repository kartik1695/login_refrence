from django.db import models
from django.utils import timezone

class Employee(models.Model):
    emp_id = models.IntegerField( blank=False, primary_key=True , unique=True , verbose_name="Employee ID")
    emp_name = models.CharField(blank =False , max_length = 30)                           
    emp_email = models.EmailField(blank= True)
    date_of_entry =  models.DateField(auto_now=True)
    emp_persona = models.CharField(max_length = 2)
    emp_state = models.CharField(max_length = 20)

    def __str__(self):
        """String for representing the Model object."""
        return self.emp_name

    class Meta:
        ordering = ["-date_of_entry",]



# Create your models here.
