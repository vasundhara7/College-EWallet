from django.shortcuts import render
from mess.models import Coupons, Orders
from usermess.models import CouponsBought,OrdersBought
from canteen.models import Payment
from django.contrib.auth.decorators import login_required
from dashboard.models import Profile
from student.models import student

#for GeneratePDF
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from trans.utils import render_to_pdf #created in step 4

#for smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#for xhtml2pdf
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import *
import requests
from threading import Thread, activeCount

from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,'trans/trans.html')

@login_required(login_url='http://127.0.0.1:8000/dashboard/login')
def many(request):
    User=request.user
    details = Transact.objects.all().order_by('-Time')
    #detailsp = Payment.objects.all().filter(user=User).order_by('-PayTime')
    #detailsc = CouponsBought.objects.all().filter(email=User).order_by('-boughtTime')
    #detailso = OrdersBought.objects.all().filter(email=User).order_by('-boughtTime')
    #detailsl = student.objects.all().order_by('-date')
    #context = {'detailsp':detailsp,'detailsc':detailsc,'detailso':detailso,'detailsl':detailsl}
    context = {'details':details}
    return render(request,"trans/trans.html",context)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('trans/trans.html')

        html = template.render()
        pdf = render_to_pdf('trans/trans.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class Pdf(View):

     def get(self, request):
         User=request.user
         details = Transact.objects.all().order_by('-Time')
         today = timezone.now()
         params = {
             'today': today,
             'details':details,
             'User': User,
             'request': request
         }
         file = Render.render_to_file('trans/trans2.html', params)

         return render(request,'trans/down.html')

def new(request):
     user=request.user
     email_user = 'ewallet.iiits@gmail.com'
     email_password = 'aseproject'
     email_send = Profile.objects.get(user=user).user.email

     subject = 'test'

     msg = MIMEMultipart()
     msg['From'] = email_user
     msg['To'] = email_send
     msg['Subject'] = subject

     body = 'Hi there, sending your Invoice'
     msg.attach(MIMEText(body,'plain'))

     filename='new.pdf'
     attachment  =open(filename,'rb')

     part = MIMEBase('application','octet-stream')
     part.set_payload((attachment).read())
     encoders.encode_base64(part)
     part.add_header('Content-Disposition',"attachment; filename= "+filename)

     msg.attach(part)
     text = msg.as_string()
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login(email_user,email_password)

     server.sendmail(email_user,email_send,text)
     server.quit()

     return render(request,'trans/mail.html')
