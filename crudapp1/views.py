from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from .forms import EmployeeLeaveForm
from .models import Employeeleave


def AddEmp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/listemp')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form': form})

def ListEmp(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def DeleteEmp(request,id):
    employee = Employee.objects.get(eid=id)
    employee.delete()
    return redirect("/listemp")

def EditEmp(request,id):
    employee=Employee.objects.get(eid=id)
    print(employee)
    print(employee.ename, employee.eid)

    return render(request,'edit.html',{'employee':employee})

def UpdateEmp(request,id):
    employee=Employee.objects.get(eid=id)
    print(employee.ename , employee.eid)
    form = EmployeeForm(request.POST , instance=employee)
    #print(form.fields("eid=id"))
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/listemp")

    #return render(request,'edit.html',{'employee':employee})
    return render(request,'edit.html',{'employee': employee})

def AddLeave(request):
    if request.method == "POST":
        form = EmployeeLeaveForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/listleave')
            except:
                pass
    else:
        form= EmployeeLeaveForm()
    return render(request,'leavecreate.html',{'form': form})


def ListLeave(request):
    empleaves = Employeeleave.objects.all()
    return render(request,'leaveindex.html',{'empleaves':empleaves})

def DeleteLeave(request,id):
    empleave = Employeeleave.objects.get(id=id)
    empleave.delete()
    return redirect("/listleave")

def EditLeave(request,id):
    empleave= Employeeleave.objects.get(id=id)
    employee=Employee.objects.all()
    print(employee)
    #print(empleave.first_name,empleave.id)
    form = EmployeeLeaveForm()
    return render(request,'leaveedit.html',{'empleave':empleave,'employees':employee})

def UpdateLeave(request,id):
    empleave=Employeeleave.objects.get(id=id)

    form = EmployeeLeaveForm(request.POST , instance=empleave)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/listleave")

    #return render(request,'leaveedit.html',{'empleave':empleave})
    return render(request,'leaveedit.html',{'empleave': empleave})
