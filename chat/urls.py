from django.urls import path, re_path
from .views import room
from .consumers import index


app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
