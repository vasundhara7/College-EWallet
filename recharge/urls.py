from django.urls import path, include
from . import views
app_name='recharge'
urlpatterns = [
    path('', views.recharge,name='recharge'),
    path('bankpage', views.bankpage),
    path('response', views.response),
]
