from django.shortcuts import render

from .models import Student

# Create your views here.

def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request, 'index.html',context)

def insertData(request):
    data=Student.objects.all()
    context={"data":data}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        age=request.POST.get('age')

        gender=request.POST.get('gender')
        query=Student(name=name, email=email, age=age, gender=gender)
        query.save()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html',)

def updateData(request):
    return render(request, 'about.html',)

def deleteData(request):
    return render(request, 'index.html',)