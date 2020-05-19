from django.db import models

# Create your models here.


class Student(models.Model):
    name =       models.CharField(max_length=20)
    gpa =        models.DecimalField(decimal_places=2, max_digits=3)
    student_id = models.CharField(max_length=10)
    age =        models.DecimalField(max_digits=3,decimal_places=0)