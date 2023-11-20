from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from app.forms import AddForm, LoginForm, SignupForm
from django.contrib import messages
from app.models import Employee
from django.contrib.auth.decorators import login_required


# Create your views here.
login_required
def home(request):
    emp = Employee.objects.all()
    return render(request,"home.html",{'emp':emp})

def addpage(request):
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AddForm()
    return render(request,"add.html",{'form':form})

def updatepage(request,id):
    if request.method == "POST":
        emp = Employee.objects.get(id = id)
        form = AddForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request,"Update Successfully")
            return redirect("homepage")
    else:
        emp = Employee.objects.get(id = id)
        form = AddForm(instance=emp)
    return render(request,"update.html",{'form':form})

def deletepage(request,id):
    emp =Employee.objects.get(id=id)
    emp.delete()
    return redirect("homepage")

def signuppage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created Successfully! Now you are able to login ")
            return redirect("loginpage")
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})
def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("homepage")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")