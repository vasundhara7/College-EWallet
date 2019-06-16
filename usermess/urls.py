from django.urls import path,include, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name="usermess.index"),
    path('buycoupon/<int:pk>', views.buycoupon, name="usermess.buycoupon"),
    path('confirmcoupon/', views.confirmcoupon, name="usermess.confirmcoupon"),
    path('yourcoupons/', views.yourcoupons, name="usermess.yourcoupons"),
    path('writereview/', views.writereview, name="usermess.writereview"),
    path('buyorder/<int:pk>', views.buyorder, name="usermess.buyorder"),
    path('allposts/', views.allposts, name="usermess.allposts"),
    path('buyorder2/', views.buyorder2, name="usermess.buyorder2"),
    path('yourreviews/', views.yourreviews, name="usermess.yourreviews"),
    path('menu/', views.menu, name="usermess.menu"),
    path('infufbal/',views.insufbal,name="usermess.insufbal")

]
