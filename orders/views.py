from django.shortcuts import render,redirect
from .models import cart,cartitem
from products.models import product
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=cart.objects.get_or_create(
        owner=customer,
        order_status=cart.cart_stage
    )
    context={'cart':cart_obj}
    
    return render(request,'cart.html',context)
def addto_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        product_id=request.POST.get('product_id')
        qty=int(request.POST.get('quantity',1))        
        cart_obj,created=cart.objects.get_or_create(
            owner=customer,
            order_status=cart.cart_stage
        )
        proeduct=product.objects.get(pk=product_id)
        order_item,created=cartitem.objects.get_or_create(
            product=proeduct,
            owner=cart_obj           
        )
        if created:
            order_item.quantity=qty
            order_item.save()
        else:
            order_item.quantity=order_item.quantity+qty
            order_item.save()   
        
    return redirect('cart')