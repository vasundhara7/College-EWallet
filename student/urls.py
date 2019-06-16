
from django.conf.urls import url
from . import views
from django.urls import path,include, re_path
urlpatterns = [
    url('main/', views.main, name="student.main"),
    path('paysub/<str:amount>', views.paysub, name="student.paysub"),
#    url(r'result/', views.librarydues,name="result"),
]

