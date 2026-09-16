# models.py
from django.db import models
 
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    enrolled_date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.name



# username 
# password 
# email 
# firstname and last name 
# is_active , is_staff and is_superuser 