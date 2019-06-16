from django.db import models

# Create your models here.
class librarian(models.Model):
    student_ID = models.CharField(max_length=100)
    book_ID =  models.CharField(max_length=100,primary_key=True)
    date = models.DateField()
    due = models.IntegerField(null = True)
    def __str__(self):
        return self.student_ID



