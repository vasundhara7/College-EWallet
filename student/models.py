from django.db import models
from dashboard.models import Profile

# Create your models here.


class student(models.Model):
    toprofile = models.ForeignKey(Profile, on_delete = models.PROTECT, default="")
    student_ID = models.CharField(max_length=100)
    book_ID =  models.CharField(max_length=100)
    date = models.DateField()
    days_left=models.IntegerField()
    due=models.IntegerField()

    def __str__(self):
        return self.student_ID



