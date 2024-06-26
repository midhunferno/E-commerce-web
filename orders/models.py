from django.db import models
from customers.models import customer
from products.models import product

# Create your models here.
class cart(models.Model):
    live=1
    delete=0
    delete_choice=((live,'live'),(delete,'delete'))
    cart_stage=0
    order_confform=1
    order_prossed=2
    order_deliverd=3
    order_rejected=4
    static_choice=(
                   (order_prossed,'order_prossed'),
                   (order_deliverd,'order_deliverd'),
                   (order_rejected,'order_rejected'),                 
                   )
    order_status=models.IntegerField(choices=static_choice,default=cart_stage)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name="orders")
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    # def __str__(self) -> str:
    #       return "cart-{}-{}".format(self.id,self.owner.user.username)

class cartitem(models.Model):
        product=models.ForeignKey(product,on_delete=models.SET_NULL,related_name="add_cart",null=True)
        quantity=models.IntegerField(default=1)
        owner=models.ForeignKey(cart,on_delete=models.CASCADE,related_name="added_item",null=True)
   