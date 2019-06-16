from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from mess.forms import PostForm
from .models import Coupons, Orders, Posts
from django.utils import timezone
from usermess.models import CouponsBought, Reviews, OrdersBought


# Create your views here.


@login_required(login_url='/dashboard/login')
def index(request):
    # Create your views here.
    if(request.user.username== 'mess'):
        posts = Posts.objects.all().order_by("-addTime")[:2]
        allorders = OrdersBought.objects.all()
        data = Orders.objects.all()
        context = {'data': data, 'posts':posts,'allorders':allorders}
        return render(request, "mess/index.html", context)
    else:
        return redirect('/dashboard/login')

@login_required(login_url='/dashboard/login')
def addcoupon(request):
    if (request.user.username == 'mess'):
        print(request.POST)
        amount = request.POST['amount']
        count = request.POST['count']
        addtime = timezone.now()
        if count == '0' or amount == '0' or count is None or amount is None:
            return redirect('mess.index')
        for i in range(int(count)):
            coupons = Coupons.objects.create(amount=amount, addTime=addtime)

        return redirect('mess.allcoupons')
    else:
        return redirect('/dashboard/login')


def addorder(request):
    if (request.user.username == 'mess'):
        print(request.POST)
        ordername = request.POST['orderName']
        amount = request.POST['amount']
        if amount == '' or ordername == '':
            return HttpResponse("Enter valid details.")
        orders = Orders.objects.create(orderName=ordername, amount=amount)
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def couponsbought(request):
    if (request.user.username == 'mess'):
        coupons = CouponsBought.objects.all().order_by('-boughtTime')
        context={"coupons":coupons}
        return render(request,"mess/couponsbought.html",context)
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def postdetails(request,id):
    if (request.user.username == 'mess'):
        post = Posts.objects.get(postId=id)
        context ={'post':post}
        return render(request,"mess/postdetails.html",context)
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def deleteorder(request):
    if (request.user.username == 'mess'):
        print(request.POST)
        u = Orders.objects.get(orderId=request.POST['orderid'])
        u.delete()
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def addpost(request):
    if (request.user.username == 'mess'):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.addTime = timezone.now()
                post.save()
                return redirect('mess.index')
        else:
            form = PostForm()
        return  render(request,"mess/postedit.html",{'form':form})
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def editpost(request,pk):
    if (request.user.username == 'mess'):
        post = get_object_or_404(Posts,postId=pk)
        if request.method== 'POST':
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                return redirect('mess.index')
        else:
            form=PostForm(instance=post)
            return render(request,"mess/postedit.html",{'form':form})
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def deletepost(request,pk):
    if (request.user.username == 'mess'):
        post = get_object_or_404(Posts,postId=pk)
        post.delete()
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def reviews(request):
    if (request.user.username == 'mess'):
        reviews = Reviews.objects.all().order_by('-reviewId')
        context = {'reviews':reviews}
        return render(request,'mess/reviews.html',context)
    else:
        return redirect('/dashboard/login')



def offers(request):
    return render(request,'mess/offers.html')


@login_required(login_url='/dashboard/login')
def deleteorderbought(request,pk):
    if (request.user.username == 'mess'):
        order = OrdersBought.objects.get(pk=pk)
        order.delete()
        posts = Posts.objects.all().order_by("-addTime")
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def changevalid(request,pk):
    if (request.user.username == 'mess'):
        order = Orders.objects.get(orderId=pk)
        if (order.valid == 1):
            Orders.objects.filter(orderId=pk).update(valid=0)
            return redirect('mess.index')
        Orders.objects.filter(orderId=pk).update(valid=1)
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')

@login_required(login_url='/dashboard/login')
def allcoupons(request):
    if (request.user.username == 'mess'):
        coupons = Coupons.objects.all().filter(valid=1).values('amount').distinct()
        couponcount=[]
        for coupon in coupons:
            coupon['count']=Coupons.objects.all().filter(valid=1).filter(amount=coupon['amount']).count()

        return render(request,"mess/allcoupons.html",{'coupons':coupons})
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def allposts(request):
    if (request.user.username == 'mess'):
        posts = Posts.objects.order_by('-addTime')
        return render(request,"mess/allposts.html",{'posts':posts})
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def deletecoupons(request,amount):
    if (request.user.username == 'mess'):
        coupons = Coupons.objects.all().filter(valid=1).filter(amount=amount)
        coupons.delete()
        return redirect('mess.allcoupons')
    else:
        return redirect('/dashboard/login')

@login_required(login_url='/dashboard/login')
def confirmcode(request):
    if (request.user.username == 'mess'):
        print(request.POST)
        code=request.POST['code']
        coupon={}
        if(Coupons.objects.filter(slug=code).exists()):
            coupons=Coupons.objects.get(slug=code)
            coupon = CouponsBought.objects.filter(couponId=coupons.couponId)
        return render(request,'mess/confirmcode.html',{'coupons':coupon})
    else:
        return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')
def deleteconfirmedcoupon(request,pk):
    if (request.user.username == 'mess'):
        coupon=Coupons.objects.get(couponId=pk)
        coupond=CouponsBought.objects.get(couponId=pk)
        coupond.delete()
        coupon.delete()
        return redirect('mess.index')
    else:
        return redirect('/dashboard/login')
