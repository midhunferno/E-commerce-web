
from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ 
    path('index',views.index,name='index'),
    path('pro_list',views.list_product,name='list_pro'),
    path('pro_detail/<pk>',views.detail_product,name='pro_detail'),
    path('contact',views.contact,name='contact')

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
