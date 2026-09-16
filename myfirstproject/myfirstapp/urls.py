from django.urls import path
from . import views

urlpatterns = [
    path('addstudent/' , views.add_student, name="add_student"),
    path('signup/' , views.signup, name="signup"),
    path('login/' , views.user_login, name="login"),
    path('logout/' , views.user_logout, name="logout"),

]


# Defination of Authentication 

# Authentication = ap kon ho ?
# Authorization = ap ko kya krny ki ijazat hy 