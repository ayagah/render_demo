from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=10,unique=True)
    date_registered=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}    {self.roll_number}    {self.date_registered}"