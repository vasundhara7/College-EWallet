from django.contrib import admin
from .models import Coupons, Orders, Posts
# Register your models here.
admin.site.register(Coupons)
admin.site.register(Orders)
admin.site.register(Posts)