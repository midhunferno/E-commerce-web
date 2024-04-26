from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def list_product(request):
    """__summary_
    returns product list page
    Args:
        request(_type_):_description_
    Returns:
         _type_:_description_    
    """
    pro_list=product.objects.all()
    context={
        'product':pro_list
        
    }
    return render(request,'product.html',context)

def detail_product(request):

    return render(request,'pro_details.html')

