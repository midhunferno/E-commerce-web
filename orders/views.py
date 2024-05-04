from django.shortcuts import render,redirect
from .models import cart,cartitem
from products.models import product
from django.contrib import messages
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

def remove_cart(request,pk):
    item=cartitem.objects.get(pk=pk)
    if item:
     item.delete()    
    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        try:
            user=request.user
            customer=user.customer_profile       
            total= float(request.POST.get('total'))        
            order_obj=cart.objects.get(
                owner=customer,
                order_status=cart.cart_stage
            )
            if order_obj:
             order_obj.order_status=cart.order_confform
             order_obj.total_price=total
             order_obj.save()
             stat_msg = "Your order has been processed. It will be delivered in 4 days."
             messages.success(request,stat_msg)
            else:
             stat_msg="Unable to process the order."           
             messages.error(request,stat_msg)
        except Exception as e:
           stat_msg="Unable to process the order. An error occurred during delivery."
           messages.error(request,stat_msg)
    return redirect('cart')             
            