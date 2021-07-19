from builtins import Exception
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm,PatientForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Department,Doctor,Patient
from django.shortcuts import render, HttpResponse, get_object_or_404



# Create your views here.
def index(request):
    return render(request,'index.html')

def app_det(request):
    return render(request,'app_details.html')

def department(request):
    department=Department.objects.all()
    return render(request,'department.html',{'obj':department})

def doctor(request):
    doctor=Doctor.objects.all()
    return render(request, 'doctor.html', {'obj': doctor})

def user_signup(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form =RegisterForm()
    return render(request, "signup.html", {"form": form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            # username=form.cleaned_data('username')
            # password=form.cleaned_data('password')
            # user=authenticate(username=username,password=password)
            # if user is not None:
            user=form.get_user()
            login(request,user)
                # messages.info(request,f"You are now logged in as {username}.")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"login_form":form})

def user_logout(request):
    # if request.method=="POST":
    logout(request)
    return redirect('/')


def appoinment(request):
    form = PatientForm()
    context = {}
    initial_dict = {
        'user':request.user,
    }
    form = PatientForm(request.POST or None,initial=initial_dict)
    context['form'] = form
    if request.method == "POST":
        form = PatientForm(request.POST or None,initial=initial_dict)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, "Success, we will contact you soon...")
            return redirect('app_det')
    return render(request, "appoinment.html", context)






    # if request.method == "POST":
    #     context = {}
    #     form = PatientForm(request.POST)
    #     if form.is_valid():
    #     # save the form data to model
    #         form.save()
    #         messages.success(request,"Success, we will contact you soon...")
    #         return redirect('/')
    #
    #     context['form'] = form
    # return render(request, "appoinment.html", context)


def dep_detail(request,slug):
    try:
        detail=Department.objects.get(slug=slug)
    except Exception as e:
        raise e
    return render(request,'dep_detail.html',{'detail':detail})

def doc_detail(request,slug):
    try:
        detail=Doctor.objects.get(slug=slug)
    except Exception as e:
        raise e
    return render(request,'doc_detail.html',{'doc':detail})

def app_det(request):
    try:
        detail=Patient.objects.get(user=request.user)
    except Exception as e:
        detail=None
    return render(request,'app_details.html',{'doc':detail})









