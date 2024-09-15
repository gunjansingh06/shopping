from django.db import models
from myadmin.models import *
from django.contrib.auth.models import User


class Saler_reg(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    shop_contact = models.BigIntegerField()
    image = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,default='Pending')
    date = models.DateField(null=True, blank=True)
        

    class Meta():
        db_table ='saler_reg'

class Product(models.Model):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    subcategories = models.ForeignKey(Subcategories,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.BigIntegerField()
    details = models.TextField()
    quantity = models.BigIntegerField()
    saler_reg=models.ForeignKey(Saler_reg,on_delete=models.CASCADE)
    size = models.CharField(max_length=255,default="")

    def __str__(self):
            return self.product_name

    class Meta():
        db_table = 'product'


