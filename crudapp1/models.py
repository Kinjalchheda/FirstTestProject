from django.db import models

# Create your models here.
from django import forms
from django.core import validators

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    ecity = models.CharField(max_length=100)
    esalary = models.IntegerField(default=0)
    def __str__(self):
        return self.ename

class Meta:
    db_table="employee"

class Employeeleave(models.Model):
    first_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
    leave_days=models.CharField(max_length=25)
    leave_reason=models.CharField(max_length=300)

class Meta:
    db_table="empleave"
