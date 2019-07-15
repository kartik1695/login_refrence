from django.shortcuts import render , get_object_or_404
from login.models import Employee
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import views

def login(request):
    context = {}
    pas = 'hello'
    if (request.method == 'POST' and request.POST['password'] == pas) :

        emp_id = request.POST['username']

        try:
            Employee.objects.get(emp_id = emp_id) 
            context['errors'] = 'yaya signed in'                
            return render(request, "login.html" , context) 
        except Employee.DoesNotExist:
            context['errors'] = 'User does not exist!!'             
            return render(request, "login.html" ,context)  
        except ValueError:
            context['errors'] = 'User does not exist!!'             
            return render(request, "login.html" , context)
    else: 
        return render(request, "login.html" ,context)

def success(self):
    pass
