
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    live=1
    delete=0
    delete_choice=((live,'live'),(delete,'delete'))
    name=models.CharField(max_length=30)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer_profile")
    phone=models.IntegerField()
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return self.name