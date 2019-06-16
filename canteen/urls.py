from django.urls import path, include, re_path
from canteen import views

app_name='canteen'

urlpatterns = [
    re_path('^$',views.index,name="canteen.index"),
    path('finishpay/', views.finishpay,name="finishpay"),
    path('order/', views.order,name="order"),
    path('vendor/',views.vendor),
    path('request/', views.Paymentreq),
    path('confirmpay/', views.confirmpay,name='confirmpay'),
]
