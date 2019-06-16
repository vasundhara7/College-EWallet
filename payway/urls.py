from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.paywaylogview.as_view()),

]
