from django import forms

from .models import OrdersBought

class OrderForm(forms.ModelForm):

    class Meta:
        model = OrdersBought
        fields = ('orderId','delTime',)
