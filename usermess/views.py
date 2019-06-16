from datetime import timedelta, datetime
from dashboard.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from mess.models import Coupons, Orders, Posts
from django.utils import timezone
# Create your views here.
from usermess.forms import OrderForm
from usermess.models import CouponsBought, Reviews, OrdersBought
from recharge import views as recharge
from trans.models import *
@login_required(login_url='/dashboard/login')
def index(request):
    user = request.user
    coupons = Coupons.objects.all().filter(valid=1)#.values('amount').distinct()

    orders = Orders.objects.all().filter(valid=1)
    posts = Posts.objects.all().order_by('-addTime')[:2]
    yourorders = OrdersBought.objects.filter(email=user).order_by('delTime')
    context = {"coupons": coupons, "orders": orders,"posts":posts,'yourorders':yourorders,'user':user}
    return render(request, "usermess/index.html", context)


@login_required(login_url='/dashboard/login')
def confirmcoupon(request):
    print(request.POST)
    couponid = int(request.POST['couponId'])
    coupon = Coupons.objects.all().filter(couponId=couponid)
    context = {"coupon": coupon}
    return render(request, "usermess/confirmcoupon.html", context)

@login_required(login_url='dashboard/login')
def buycoupon(request,pk):
    coupon = get_object_or_404(Coupons,pk=pk)
    amount = coupon.amount
    balance = Profile.objects.get(user = request.user).balance
    if(amount>balance):
        return redirect('usermess.insufbal')
    balance = balance - amount
    Profile.objects.filter(user=request.user).update(balance=balance)
    if Profile.objects.filter(user__username='mess').exists():
        balance2 = Profile.objects.get(user__username = 'mess').balance
        Profile.objects.filter(user__username='mess').update(balance=balance2 + amount)
    coupon=Coupons.objects.all().filter(couponId=pk)
    if (Coupons.objects.get(couponId=pk).valid==0):
        return render(request,"usermess/errorcoupon.html")
    context = {"coupon": coupon}
    update = Coupons.objects.filter(couponId=pk).update(valid=0)
    create =  CouponsBought.objects.create(couponId_id=pk,boughtTime=timezone.now(),email=request.user)
    t=Transact.objects.create(Amount=amount,Time=timezone.now(),Recipient='mess vendor')
    return render(request,"usermess/buycoupons.html",context)

@login_required(login_url='/dashboard/login')
def yourcoupons(request):
    coupons = CouponsBought.objects.filter(email=request.user)
    context = {"coupons": coupons}
    return render(request, "usermess/yourcoupons.html", context)


@login_required(login_url='/dashboard/login')
def writereview(request):
    print(request.POST)
    subject = request.POST['reviewsubject']
    body = request.POST['reviewbody']
    if not(subject is None or body is None):
        reviews = Reviews.objects.create(subject=subject,body=body,user=request.user)
        return redirect('usermess.yourreviews')
    else :
        return redirect('usermess.index')


@login_required(login_url='/dashboard/login')
def buyorder(request,pk):
    order = Orders.objects.get(orderId=pk)
    return render(request,"usermess/buyorder.html",{'order':order})



@login_required(login_url='/dashboard/login')
def allposts(request):
    posts = Posts.objects.all().order_by('-addTime')
    return render(request,'usermess/allposts.html',{'posts':posts})

@login_required(login_url='/dashboard/login')
def buyorder2(request):
    print(request.POST)
    orderId=request.POST['orderId']
    order=Orders.objects.get(orderId=orderId)
    delTime=request.POST['delTime']
    if(orderId is None or order is None or delTime is None):
        return redirect(buyorder,orderId)
    try:
        date=datetime.strptime(delTime, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return redirect(buyorder,orderId)
    if (date-datetime.now()<=timedelta(hours=2)):
        return redirect(buyorder,orderId)

    email=request.user
    ordercreate=OrdersBought.objects.create(orderId=order,delTime=delTime,boughtTime=timezone.now(),email=email)
    return redirect('usermess.index')

@login_required(login_url='/dashboard/login')
def yourreviews(request):
    reviews = Reviews.objects.all().filter(user=request.user)
    return render(request,'usermess/yourreviews.html',{'reviews':reviews})


def menu(request):
    return render(request,"usermess/menu.html")


def insufbal(request):
    return render(request,'usermess/insufbal.html')
