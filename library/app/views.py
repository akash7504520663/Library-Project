from django.shortcuts import render

# Create your views here.
from app.models import *

def student(request):
    SO=Student.objects.all()
    d={'SO':SO}
    if request.method=='POST':
        name=request.POST['sn']
        BO=Book.objects.all()
        d={'name':name,'BO':BO}
        return render(request,'home.html',d)
    return render(request,'student.html',d)