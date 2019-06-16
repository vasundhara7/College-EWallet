from django.db import models
# Create your models here.
class Transact(models.Model):
    TransId = models.AutoField(primary_key=True,null=False)
    Time = models.DateTimeField()
    Amount = models.IntegerField(null=False)
    Recipient = models.CharField(max_length=200)
