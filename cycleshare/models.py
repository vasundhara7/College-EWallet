from django.db import models
from dashboard.models import Profile

class Cycle(models.Model):
    toprofile = models.ForeignKey(Profile, on_delete = models.CASCADE, default="")
    fullname = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True,null=True)
    hour = models.IntegerField(null =False, default=0)
    type = models.CharField(max_length=100,null=True)
    hour_sub = models.FloatField(null=True)

    def __str__(self):
        return self.fullname

class availability(models.Model):

    type1 = models.IntegerField()
    type2 = models.IntegerField()
    type3 = models.IntegerField()







