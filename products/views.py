from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featuerd_pro=product.objects.order_by('prioraty')[:4]
    letast_pro=product.objects.order_by('-id')[:4]
    context={
        'featuerd_pro':featuerd_pro,
        'letast_pro':letast_pro
    }

    return render(request,"index.html",context)

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
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    pro_list=product.objects.order_by('prioraty')
    pro_page=Paginator(pro_list,4)
    pro_list=pro_page.get_page(page)
    context={
        'product':pro_list
        
    }
    return render(request,'product.html',context)

def detail_product(request, pk):
    pro=product.objects.get(pk=pk)
    context={
        'product':pro
    }
    return render(request,'pro_details.html',context)

