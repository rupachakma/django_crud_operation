from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=50)
    profileimg = models.ImageField(upload_to="img",blank=True,null=True)
    createat = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
