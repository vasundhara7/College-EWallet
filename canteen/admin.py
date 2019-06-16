from django.contrib import admin
from .models import Payment, Order, card_pay

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(card_pay)
