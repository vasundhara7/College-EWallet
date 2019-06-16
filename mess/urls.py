from django.urls import path,include, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name="mess.index"),
    path('result/', views.addcoupon, name="mess.addcoupon"),
    path('addorder/', views.addorder, name="mess.addorder"),
    path('allposts/', views.allposts, name="mess.allposts"),
    path('allcoupons/', views.allcoupons, name="mess.allcoupons"),
    path('couponsbought/', views.couponsbought, name="mess.couponsbought"),
    path('postdetails/<int:id>', views.postdetails, name="mess.postdetails"),
    path('deleteorder/',views.deleteorder,name="mess.deleteorder"),
    path('addpost/',views.addpost,name="mess.addpost"),
    path('post/<int:pk>/edit/', views.editpost, name='mess.editpost'),
    path('post/<int:pk>/delete', views.deletepost,name='mess.deletepost'),
    path('reviews', views.reviews, name='mess.reviews'),
    path('deleteorderbought/<int:pk>/', views.deleteorderbought, name="mess.deleteorderbought"),
    path('changevalid/<int:pk>/', views.changevalid, name="mess.changevalid"),
    path('deletecoupons/<str:amount>/', views.deletecoupons, name="mess.deletecoupons"),
    path('confirmcode/', views.confirmcode, name="mess.confirmcode"),
    path('deleteconfirmedcoupon/<int:pk>', views.deleteconfirmedcoupon, name="mess.deleteconfirmedcoupon"),
]
