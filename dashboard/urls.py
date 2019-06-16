from django.conf.urls import url, include
from . import views
from django.urls import path

from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^account/$', views.account, name='account'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),

    path('accounts/', views.accounts, name='accounts'),
    path('explore/',views.explore,name='explore'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('payments/', views.payments, name='payments'),
    path('pay/', views.pay, name='pay'),
    path('pay_a_friend/',views.pay_a_friend,name='pay_a_friend'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='dashboard/homepage.html'), name='logout'),
    url(r'^password/$', views.change_password, name='change_password'),

    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

]
