"""ewallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
from forms_builder.forms import views
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from mess import views as viewsm
from django.shortcuts import render
from forms_builder.forms.models import Form
from forms_builder.forms.views import FormDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recharge/', include('recharge.urls')),
    path('dummybank/', include('dummybank.urls')),
    path('mess/', include('mess.urls')),
	re_path(r"forms/(?P<slug>.*)/sent/$", views.form_sent, name="form_sent"),
	re_path(r"forms/(?P<slug>.*)/$", FormDetail.as_view(template_name="formview.html"),name="form_detail"),
    #path('forms/', lambda request: render(request, "formpage.html", {"forms": Form.objects.all()})),
    path('usermess/', include('usermess.urls')),
    path('dashboard/', include('dashboard.urls')),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='dashboard/password_reset_form.html',
                                                            email_template_name="dashboard/reset_password_email.html",
                                                            success_url="done/"), name="password_reset"),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='dashboard/password_reset_done.html'),
            name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(template_name="dashboard/password_reset_confirm.html"),
            name="password_reset_confirm"),
    url(r'^reset-password/complete/$',
            PasswordResetCompleteView.as_view(template_name="dashboard/password_reset_complete.html"),
            name="password_reset_complete"),
    url(r'^cycleshare/', include('cycleshare.urls')),
    url(r'^librarian/', include('librarian.urls')),
    url(r'^student/', include('student.urls')),
    path('canteen/',include('canteen.urls')),
	path('chat/', include('chat.urls', namespace='chat')),
    path('', include('dashboard.urls')),
    path('offers/',viewsm.offers,name='mess.offers'),
    path('api/pay/', include('payway.urls')),
    path('trans/', include('trans.urls')),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
