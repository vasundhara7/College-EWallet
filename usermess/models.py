

from django.db import models
from mess.models import Coupons, Orders
from django.utils import timezone
# Create your models here.


class CouponsBought(models.Model):
    couponId = models.ForeignKey(Coupons, on_delete=models.PROTECT)
    boughtTime = models.DateTimeField()
    email = models.CharField(max_length=150)



class Reviews(models.Model):
    reviewId = models.AutoField(primary_key=True)
    subject = models.TextField(null=False)
    body = models.TextField(null=False)
    user = models.CharField(max_length=150,null=False)
    def __str__(self):
        return(self.subject)

class OrdersBought(models.Model):
    orderId = models.ForeignKey(Orders, on_delete=models.PROTECT)
    boughtTime = models.DateTimeField(null=False)
    delTime = models.DateTimeField( )
    email = models.CharField(max_length=150)
    def __str__(self):
        return(self.orderId.orderName)
