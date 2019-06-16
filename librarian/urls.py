
from django.conf.urls import url
from . import views

urlpatterns = [
    url('input/', views.library, name="librarian.library"),
    url(r'result/', views.lbran,name="result"),
    url(r'all/', views.view ,name="view"),
    url(r'new/', views.new ,name="new"),
]
