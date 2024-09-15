from django.db import models
from myadmin.models import *
from seller.models import *
from django.contrib.auth.models import User

class Register(models.Model):
    address = models.TextField()
    contact  = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,default='Pending')
    date = models.DateField(null=True, blank=True)

    class Meta():
        db_table = 'register'

class Contact(models.Model):
    name    = models.CharField(max_length=150)
    email   = models.CharField(max_length=150)
    contact = models.BigIntegerField()
    message = models.TextField()
    date = models.DateField()
    

    class Meta():
        db_table = 'contact'

class Cart(models.Model):
    quantity = models.CharField(max_length=255,default='1')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    saler = models.ForeignKey(Saler_reg,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=255,default='')


    class Meta():
        db_table = 'cart'

class Order(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    status = models.CharField(max_length=255,default='Pending')
    saler = models.ForeignKey(Saler_reg,on_delete=models.CASCADE)
    pay_method = models.CharField(max_length=255)

    class Meta():
        db_table = 'order'

class Shipping(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    address = models.TextField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    pincode = models.BigIntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.BigIntegerField()
    amount = models.BigIntegerField()

    class Meta():
        db_table = 'shipping'

class Billing(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    address = models.TextField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    pincode = models.BigIntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.BigIntegerField()
    amount = models.BigIntegerField()

    class Meta():
        db_table = 'billing'

class Order_details(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255,default='1')
    amount = models.BigIntegerField()
    size = models.CharField(max_length=255)


    class Meta():
        db_table = 'order_details'
