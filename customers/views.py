from django.shortcuts import render ,redirect
from .models import customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def custamer_reg(request):
    context={}
    if request.POST and 'register' in request.POST:  
        context['register'] =True   
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('number')
        address=request.POST.get('address')
        password=request.POST.get('password')  
        if User.objects.filter(username=username).exists():
           err="username already exist"
           return render(request,'account.html',{'err':err})
        else:    
         user=User.objects.create_user(
            username=username,
            email=email,           
            password=password
        )
        costomer=customer.objects.create(
            user=user,
            phone=phone,
            address=address
        )
        costomer.save()
        return redirect('account')
    
    if request.POST and 'login' in request.POST:
         context['register']=False
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(request,username=username,password=password)
         if user:
            login(request,user)
            return redirect('index')
         elif not user:
            err1="invalid user !"
            return render(request,'account.html',{'err':err1})
    return render(request,'account.html',context)

def userlogout(request):
   logout(request)
   return redirect('account')
