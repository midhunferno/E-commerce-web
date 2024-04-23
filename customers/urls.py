from django.urls import path
from customers import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('account',views.custamer_login,name='account')
]