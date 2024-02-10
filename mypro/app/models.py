from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=250)
    nickname=models.CharField(max_length=250)
    birthdate=models.CharField(max_length=10)
    gardion=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    nationality=models.CharField(max_length=250)
    cls=models.CharField(max_length=250)
    address=models.CharField(max_length=550)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=250)
    teacher=models.CharField(max_length=250)
    enrollmentdate=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    sub=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    zip=models.CharField(max_length=6)
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name