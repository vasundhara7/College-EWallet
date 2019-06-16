from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import student
from librarian.models import librarian
from datetime import datetime as dt
from datetime import date
from dashboard.models import Profile

def main(request):
    us = request.user
#    no = 20170020236
#    no = librarian.objects.get(student_ID = )
    no = Profile.objects.get(user = us).student_id
    print("working")
#    ob = librarian.objects.filter(student_ID=no).get()
    ob = librarian.objects.raw("SELECT book_ID from librarian_librarian where student_ID='"+str(no)+"';")
    context={}
    ls = []
    for ab in ob:
        df = {  }
        df['details']= ab
        d = str(ab.date).split('-')
        d2 = date(int(d[0]), int(d[1]), int(d[2]))
        d1 = date(dt.now().year,dt.now().month,dt.now().day)
        dl = (d1-d2).days
        df['days_left'] = 15-dl
        if df['days_left']<0:
            df['due'] = df['days_left']*-4
            df['paynow'] = 1
        else:
            df['due'] = 0
            df['paynow'] = 0
        ls.append(df)
    context['details'] = ls
    print(context)
    return render(request, "student/student.html", context)
#    return HttpResponse('succesfully updated')

def daysleft(request):
    return render(request,'librarian/librarian.html')
def paysub(request,amount):
    amount=int(float(amount))
    user=request.user
    balance=Profile.objects.get(user=user).balance
    if(amount>balance):
        return redirect('/recharge')
    Profile.objects.filter(user=user).update(balance=balance-amount)


    return render(request,"student/ok.html")