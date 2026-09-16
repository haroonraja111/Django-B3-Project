from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.http import HttpResponse
from .forms import StudentForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm()
    return render (request , 'myfirstapp/add_student.html' , {'form' : form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render (request , 'myfirstapp/signup.html' , {'form' : form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render (request , 'myfirstapp/login.html' , {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request,'myfirstapp/dashboard.html')



# Decorator @login_required
# Template Inheritance or Static Files 
# base.html , extand and block tags











# # myapp/views.py
 
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
 
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})










# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('full_name')
#         message = request.POST.get('message')
#         print(name, message)
#     return render(request, 'myfirstapp/home.html')



# def contact(request):
#     form = ContactForm()
#     return render(request , 'myfirstapp/home.html' , {'form' : form})


