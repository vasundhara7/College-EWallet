from django.contrib import admin
from .models import CouponsBought, Reviews, OrdersBought

# Register your models here.
admin.site.register(CouponsBought)
admin.site.register(Reviews)
admin.site.register(OrdersBought)