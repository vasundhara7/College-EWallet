from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from dashboard import models
from dashboard.models import Profile
from dashboard.choices import *


class UserRegisterForm(UserCreationForm):
    #username = forms.CharField(label='Your name',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})
    student_id=forms.CharField(min_length=12,max_length=12,required=True,widget=forms.TextInput())
    phone_number=forms.CharField(min_length=10,max_length=10,required=True,widget=forms.TextInput())
    role=forms.ChoiceField(choices=ROLE_CHOICES,label='Type of account',initial='', widget=forms.Select(), required=True)
    year=forms.ChoiceField(choices=YEAR_CHOICES,label='Year of study',initial='',widget=forms.Select(), required=True)
    picture=forms.ImageField( required=False )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["iiits.in",]

        if domain not in domain_list:
            raise forms.ValidationError("Please enter an Email Address with a valid domain")
        if User.objects.filter(email=data).exists():
            raise  forms.ValidationError("User with the email id already exists.")
        return data



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email',]

class UserProfileForm(forms.ModelForm):

    card_id=forms.CharField(required=False)

    class Meta:
        model=Profile
        fields=['phone_number','card_id' ,'picture', ]

    def save(self, user=None):
        user_profile=super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user=user
        user_profile.save()
        return user_profile