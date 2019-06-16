from django.shortcuts import render
import hashlib
from django.contrib.auth.models import User
from dashboard.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='dashboard:login')
def recharge(request):
    username = request.user
    balance = Profile.objects.get(user = username).balance
    if request.method == 'POST':
        mkey = '#'
        salt = '#'
        firstname = 'anirudh'
        email = 'anirudhambati@gmail.com'
        phone = '9959295327'
        productdesc = 'recharge'
        hash_object = hashlib.sha256(b'randint(0,20)')
        txnid = hash_object.hexdigest()[0:20]

        amount = request.POST['amount']
        he = mkey+'|'+txnid+'|'+str(amount)+'|'+productdesc+'|'+firstname+'|'+email+'|||||||||||'+salt
        hashfn = str.lower( hashlib.sha256(he.encode('utf-8')).hexdigest() )
        data = {'amount': float(amount), 'firstname': firstname, 'email': email, 'phone':phone, 'product':productdesc, 'txnid':txnid, 'hash':hashfn, 'mkey':mkey, 'salt':salt, 'balance':balance}

        return render(request, 'recharge/dtransaction.html', data)
    else:
        return render(request, 'recharge/recharge.html', {'balance':balance})

def bankpage(request):
    amount = request.POST['amount']
    return render(request, 'recharge/index.html', {'amount':amount})

def response(request):
    amount = request.POST['amount']
    status = request.POST['status']
    username = request.user
    balance = Profile.objects.get(user = username).balance

    if status=='1':
        message = 'Your Transaction for Rs: '+ amount + ' has been successful!!'
        status = 'successful'
        balance += int(float(amount))
        Profile.objects.filter(user = username).update(balance = balance)
    else:
        message = 'Your Transaction has failed!'
        status = 'failed'
    return render(request, 'recharge/response.html', {'status':status, 'amount':amount, 'message':message})
