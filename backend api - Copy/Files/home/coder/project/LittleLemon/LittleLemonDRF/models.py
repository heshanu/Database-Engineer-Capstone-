from django.db import models
from django.contrib.auth.models import User

#from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from django.forms import ModelForm

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   image=models.CharField(max_length=200,default="test/1.jpg") 

   def __str__(self):
      return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    price=models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        unique_together=('menuitem','user')

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='delivery_crew',null=True)
    status=models.BooleanField(db_index=True,default=0)
    total=models.DecimalField(max_digits=6,decimal_places=2)
    date=models.DateField(db_index=True)

class OrderItem(models.Model):
    order=models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    price=models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        unique_together=('order','menuitem')

