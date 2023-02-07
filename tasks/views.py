from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

from tasks.models import *
from .forms import *

def index(request):
    tasks=Task.objects.all()
    form= TaskForm()

    context={'tasks':tasks,'form':form}
    return render(request, 'list.html', context)


def signin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        a=data.objects.all()
        for i in a:
            if uname == i.uname and passw == i.passw:
                fi(uname)
                return redirect('/index')
        #Data=data(uname=uname, passw=passw)
        return "invalid username or password"
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        a=data.objects.all()
        for i in a:
            if uname == i.uname:
                return "user already exist, please login"
        Data=data(uname=uname, passw=passw, email=email)
        Data.save()
        fi(uname)
        return redirect('/index')
def fi(uname):
    f=open("user.user", "w")
    f.write(uname)
    f.close()
    print(145)

def index(request):
    f=open("user.user", 'r')
    u=f.read()
    print(u)
    f.close()
    tasks=Task.objects.all()
    form =TaskForm()
    if request.method=='POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)    
    if request.method == 'POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {'form':form}
    return render(request, 'update.html', context)

def deleteTask(request, pk):
    item=Task.objects.get(id=pk)
    d=Task.objects.filter(id=pk).delete()
    context={'item':item}
    return render(request, 'delete.html')

def logout(request):
    print("logout")
    f=open('user.user', 'w')
    f.write('q')
    f.close()
    return redirect('/')