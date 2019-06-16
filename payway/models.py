from django.db import models

# Create your models here.
class paywaylog(models.Model):
    id = models.AutoField(primary_key=True)
    cardid = models.CharField(null = False, max_length = 50)
