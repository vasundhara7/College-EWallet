from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.choices import *


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES,null=True,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    picture=models.ImageField(upload_to='profile_image', default='static/dashboard/images/default-img.png')
    phone_number = models.CharField(max_length=10,
                                    validators=[
                                        RegexValidator(
                                            regex='^[1-9]{1}[0-9]{9}$',
                                            message='Enter a valid phone number',
                                            code='invalid_cell'
                                        ),
                                    ]
                                    )
    student_id=models.CharField(max_length=12, validators=[
                                                    RegexValidator(regex='^[S]{1}[0-9]{11}$',
                                                                   message='Enter a valid student id',
                                                                   code='invalid_cell'
                                                                   ),
    ])
    balance=models.IntegerField(default=0)
    card_id=models.CharField(null=True, max_length=30)
    email_confirmed = models.BooleanField(default=False)



    def __str__(self):  # __unicode__ for Python 2
        return self.user.username



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
