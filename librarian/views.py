from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from .models import librarian


#from datetime import datetime as dt
#from datetime import datetime as dte
def library(request):
    return render(request,'librarian/librarian.html')
def lbran(request):
    if request.method == "POST":
        student_ID=request.POST['student_ID']
        book_ID = request.POST['book_ID']
        dt = request.POST['date']
        context = {'error': 0}
        if not (book_ID and student_ID and dt ):
            context['error'] = 1
        else:
            librarian.objects.create(student_ID= student_ID,  book_ID=book_ID,date=dt)
        if not context['error']:
            return render(request,'librarian/ok.html')
        else:
            return render(request, 'librarian/librarian.html',context)
    else:
         return HttpResponseRedirect('/librarian/input/')

def view(request):
    b = librarian.objects.all()
    return render(request,"librarian/all.html", {'form':b})
def new(request):
    return render(request,'librarian/new.html')