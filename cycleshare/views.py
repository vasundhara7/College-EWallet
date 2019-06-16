from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from trans.models import *
# Create your views here.
from django.shortcuts import render
from .models import Cycle,availability
from dashboard.models import Profile
from django.utils import timezone

def cycle(request):
    return render(request,'cycleshare/cycleshare.html')
def ui(request):
    return render(request, 'cycleshare/ui.html')

def available(request):
    try:
        cycles = availability.objects.get(id = 1)
        return render(request, 'cycleshare/available.html',{'cycles':cycles})
    except:
        return render(request, 'cycleshare/available.html', {'error': 'No Cylces available'})
def subscribe(request):
    return render(request,'cycleshare/subscribe.html')

def cycleshare(request):
    if request.method == "POST":
        print("Request Object:{}".format(request.POST))
        student_name = request.POST['fullname']
        student_ID = request.POST['student_ID']
        date = request.POST['date']
        hour = request.POST['hour']
        type = request.POST['type']
        context = {'error':0}
        if not (student_name and student_ID and date and hour and type):
            context['error'] = 1
        else:
            hour_sub =hour * 30
            hour_sub=int(hour_sub)
            if not Cycle.objects.filter(fullname=student_name):
                us = request.user
                no = Profile.objects.get(user=us)
                Cycle.objects.create(toprofile=no,fullname=student_name, student_ID=student_ID, date=date, hour=hour, type=type, hour_sub = hour_sub, )
            try:
                x = availability.objects.get()
                bn1 = int(x.type1)
                bn2 = int(x.type2)
                bn3 = int(x.type3)
                if type=='1':
                    availability.objects.filter().update(type1=bn1-1)
                if type=='2':
                    availability.objects.filter().update(type2=bn2-1)
                if type=='3':
                    availability.objects.filter().update(type3=bn3-1)
            except:
                pass
        #    x=availability.objetcs.raw("UPDATE availability SET type1="+str(x.type1-1)+" WHERE tpye1="+str(x.type1))
            share = Cycle.objects.get(fullname=student_name)
        if not context['error']:
            return render(request, "cycleshare/cycleshare1.html",  {'student_share': share})
        else:
            return render(request, "cycleshare/cycleshare.html", context )
    else:
        return HttpResponseRedirect('/cycleshare/input/')

def view(request):
    b = Cycle.objects.all()
    return render(request,"cycleshare/all.html", {'form':b})

def recent(request):
    us = request.user
    #    no = 20170020236
    #    no = librarian.objects.get(student_ID = )
    no = Profile.objects.get(user = us).student_id
    #no = Cycle.objects.get(toprofile=us).student_id
    print("working",no)
    #    ob = librarian.objects.filter(student_ID=no).get()
    ob = Cycle.objects.filter(student_ID = no)
    ls = []
    context = {}
    for ab in ob:
        df = {  }
        df['fullname']= ab.fullname
        df['student_id']= ab.student_ID
        df['date']= ab.date
        df['hour']= ab.hour
        df['type']= ab.type
        df['sub'] = ab.hour_sub
        ls.append(df)
    context['details'] = ls
    print(context)

    return render(request,"cycleshare/recent.html",context)
def book(request,value):
    context={'value':value}
    return render(request,"cycleshare/book.html",context);


def paysub(request,amount):
    amount=int(float(amount))
    user=request.user
    time = timezone.now()
    balance=Profile.objects.get(user=user).balance
    if(amount>balance):
        return redirect('/recharge')
    Profile.objects.filter(user=user).update(balance=balance-amount)
    t = Transact(Amount = amount, Time=time, Recipient='Cycle Vendor')
    t.save()


    return render(request,"cycleshare/ok.html")