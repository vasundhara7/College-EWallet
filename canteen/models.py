from django.db import models
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    PayId = models.IntegerField(primary_key=True,null=False)
    user = models.CharField(max_length=150,null=False,default='hem1')
    Amount = models.IntegerField()
    PayTime = models.DateTimeField( blank=True)

class Order(models.Model):
    user = models.CharField(max_length=150,null=False,default='hem1')
    Itemname = models.CharField(max_length=100)
    Quantity = models.IntegerField(null=True)
    OrderTime = models.DateTimeField( blank=True)

class card_pay(models.Model):
    id = models.AutoField(primary_key=True)
    flag = models.IntegerField()
