from django.urls import path
from orders import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('cart',views.show_cart,name='cart')
]