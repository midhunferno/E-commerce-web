from django.db import models

# Create your models here.
class product(models.Model):
    live=1
    delete=0
    delete_choice=((live,'live'),(delete,'delete'))
    title=models.CharField(max_length=30)
    price=models.FloatField()
    describtion=models.TextField()
    image=models.ImageField(upload_to='/media')
    prioraty=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self)-> str:
        return self.title
