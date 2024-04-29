from django.shortcuts import render ,redirect
from .models import customer

# Create your views here.

def custamer_login(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        address=request.POST.get('address')
        password=request.POST['password']
        Conform_Password=request.POST['cnf_pwd']
        
        costomer=customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=password,
            Conform_Password=Conform_Password
        )
        costomer.save()
        return redirect('index')

    return render(request,'account.html')