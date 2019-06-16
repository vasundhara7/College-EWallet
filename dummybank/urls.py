from django.urls import path, include
from . import views

urlpatterns = [
    path('transaction/', views.transaction),
    path('bankpage/', views.bankpage),
    path('response', views.response)
]
