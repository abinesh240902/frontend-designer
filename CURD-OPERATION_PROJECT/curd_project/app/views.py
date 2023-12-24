from django.shortcuts import render,redirect
from .models import details
from django.contrib import messages

# Create your views here.
def index(request):
    data=details.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def updatedata(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=details.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=details.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deletedata(request,id):
    d=details.objects.get(id=id)
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")

def insertdata(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query = details(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    
    return render(request,"index.html")