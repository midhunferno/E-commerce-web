from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def list_product(request):
    """__summary_
    returns product list page
    Args:
        request(_type_):_description_
    Returns:
         _type_:_description_    
    """
    return render(request,'product.html')

def detail_product(request):

    return render(request,'pro_details.html')

