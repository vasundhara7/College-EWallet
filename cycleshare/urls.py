
from django.conf.urls import url
from . import views
from django.urls import path,include, re_path
urlpatterns = [
    url(r'input/', views.cycle, name="cycleshare.cycleshare"),
    url(r'result/', views.cycleshare,name="cycleshare.result"),
    url(r'ui/', views.ui,name="cycleshare.ui"),
    url(r'available/', views.available,name="cycleshare.available"),
    url(r'subscribe/', views.subscribe,name="cycleshare.subscribe"),
    url(r'recent/', views.recent,name="cycleshare.recent"),
    url(r'all/', views.view, name="view"),
    path('book/<int:value>', views.book, name="cycleshare.book"),
    path('paysub/<str:amount>', views.paysub, name="cycleshare.paysub"),
]
0