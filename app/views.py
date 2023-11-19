
from django.shortcuts import redirect, render

from app.models import Employee


# Create your views here.
def home(request):
    emp = Employee.objects.all()
    return render(request,"home.html",{'emp':emp})