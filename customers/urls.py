from django.urls import path
from customers import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('',views.custamer_reg,name='account'),
    path('log',views.userlogout,name="logout")
    
]