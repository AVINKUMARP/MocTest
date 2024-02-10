from django.shortcuts import render
from .models import Student
from django.http import  HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    content=Student.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)

def details(request,id):
    student=Student.objects.get(pk=id)
    print(student)
    data={
        'data':student
    }
    return render(request,'details.html',data)