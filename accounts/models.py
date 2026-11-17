from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=12,unique=True)
    ROLE_CHOICES =(
        ('admin',"admin"),
        ('trainer','trainer'),
        ('student','student')
    )

ROLE=models.CharField(max_length=10,choices=ROLE_CHOICES,default='student')

class Student(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    course=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    pass_outyear=models.PositiveIntegerField()
    skills=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Trainer(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    trainer_name=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    experience=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username