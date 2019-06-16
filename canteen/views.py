from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment,Order,card_pay
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import time
from payway.models import paywaylog
from django.contrib.auth.models import User
from dashboard.models import *
from trans.models import Transact
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request,'canteen/index.html')

@login_required(login_url='http://127.0.0.1:8000/dashboard/login')
def finishpay(request):
    user = request.user
    Amount = request.POST['Amount']
    PayTime = timezone.now()
    Payment.objects.create(user=request.user,PayTime=PayTime,Amount=Amount)

    return render(request,"canteen/paypass.html")

@login_required(login_url='http://127.0.0.1:8000/dashboard/login')
def order(request):
    user = request.user
    Itemname = request.POST['item']
    Quantity = request.POST['amount']
    OrderTime = timezone.now()
    Order.objects.create(user=request.user,OrderTime=OrderTime,Itemname= Itemname,Quantity=Quantity)
    return render(request,"canteen/orderpass.html")

def vendor(request):
    detailsp = Payment.objects.all().order_by('-PayTime')
    detailso = Order.objects.all().order_by('-OrderTime')
    context = {'detailsp':detailsp,'detailso':detailso}
    return render(request,"canteen/vendor.html",context )

def Paymentreq(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        c = paywaylog.objects.all().count()
        t_end = time.time() + 15
        while time.time() < t_end:
            count2 = paywaylog.objects.all().count()
            if (count2 == (c + 1)):
                card = paywaylog.objects.last().cardid
                if Profile.objects.filter(card_id = card).exists():
                    balance = Profile.objects.get(card_id = card).balance
                else:
                    message = 'User Card declined!'
                    return render(request, 'canteen/timeout.html',{'message':message})

                if int(float(balance)) >= int(float(amount)):
                    #add for vendor
                    ####
                    #subtract from userlog
                    balance -= int(float(amount))
                    if Profile.objects.filter(card_id = card).exists():
                        Profile.objects.filter(card_id = card).update(balance = balance)
                        name = Profile.objects.get(card_id = card).user
                        number = Profile.objects.get(card_id = card).phone_number
                        return render(request, 'canteen/paysucess.html', {'amount':amount, 'number':number, 'name':name})
                    else:
                        message = 'User Card declined!'
                        return render(request, 'canteen/timeout.html',{'message':message})
                else:
                    message = 'User Card declined!'
                    return render(request, 'canteen/timeout.html',{'message':message})

            elif (count2 > c):
                message = 'An error occured, try again'
                return render(request, 'canteen/timeout.html',{'message':message})
        message = 'Payment timeout, try again'
        return render(request, 'canteen/timeout.html',{'message':message})

    return render(request, 'canteen/pay.html')

def confirmpay(request):
    print(request.POST)
    amount=int(request.POST['amount'])
    balance=Profile.objects.get(user=request.user).balance
    if amount>balance:
        return redirect('/recharge')
    user = request.user
    Amount = request.POST['amount']
    PayTime = timezone.now()
    Payment.objects.create(user=request.user,PayTime=PayTime,Amount=Amount)
    Transact.objects.create(Amount=Amount,Time=PayTime,Recipient='canteen')
    return render(request,"canteen/paypass.html")
