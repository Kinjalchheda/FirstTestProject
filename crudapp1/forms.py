from django import forms
from .models import Employee
from .models import Employeeleave
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields= "__all__"

class EmployeeLeaveForm(forms.ModelForm):
    class Meta:
        model = Employeeleave
        fields= "__all__"