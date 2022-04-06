from django.shortcuts import render,HttpResponseRedirect
from .models import lab
from .forms import insertform
from .forms import signupform,insertform,loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
  bd=lab.objects.all()
  return render(request,'index.html',{'bd':bd})

#insert
def insert_book(request):
    if request.method=="POST":
        form=insertform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=insertform()
    return render(request,'bookboard.html',{'form':form})

#delet
def delete_data(request,id):
    if request.method=="POST":
        bd=lab.objects.get(pk=id)
        bd.delete()
    return HttpResponseRedirect('/bookinfo/')

#update
def update_data(request,id):
    if request.method=="POST":
        bd=lab.objects.get(pk=id)
        form=insertform(request.POST,instance=bd)
        if form.is_valid():
            form.save()
    else:
        bd=lab.objects.get(pk=id)
        form=insertform(instance=bd)
    return render(request, 'update.html',{'form':form})
        
#fetch_data
def bookinfo(request):
    bd=lab.objects.all()
    return render(request, 'bookinfo.html',{'bd':bd})

def sign_up(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
         messages.success(request, 'congratulations become admin')
         form.save()
    else:
        form=signupform()
    return render(request,'signup.html',{'form':form})

#login
def login_admin(request):
   if not request.user.is_authenticated:
    if request.method=="POST":
       form=loginform(request=request,data=request.POST)
       if form.is_valid():
        uname=form.cleaned_data['username']
        upass=form.cleaned_data['password']
        user=authenticate(username=uname,password=upass)
        if user is not None:
         login(request, user)
        messages.success(request,'logged in successfully')
        return HttpResponseRedirect('/bookinfo/')
    else:
        form=loginform()
    return render(request,'login.html',{'form':form})
   else:
    return HttpResponseRedirect('/bookinfo/')
        

# logout
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')
        
      
        