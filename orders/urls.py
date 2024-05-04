from django.urls import path
from orders import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('cart',views.show_cart,name='cart'),
    path('addtocart',views.addto_cart,name="addtocart"),
    path('remove_cart/<pk>',views.remove_cart,name='remove_cart'),
    path('checkout/',views.checkout,name='checkout')
]