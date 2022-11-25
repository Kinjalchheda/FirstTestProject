"""crudsample1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crudapp1 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('addemp/',views.AddEmp),
    path('listemp/',views.ListEmp),
    path('deleteemp/<int:id>',views.DeleteEmp),
    path('editemp/<int:id>',views.EditEmp),
    path('updateemp/<int:id>',views.UpdateEmp),
    path('addleave/',views.AddLeave),
    path('listleave/',views.ListLeave),
    path('deleteleave/<int:id>',views.DeleteLeave),
    path('editleave/<int:id>',views.EditLeave),
    path('updateleave/<int:id>',views.UpdateLeave),

]
