from django.shortcuts import render

# Create your views here.

def transaction(request):
    amount = request.POST['amount']
    return render(request, 'dummybank/transaction.html', {'amount': amount})


def bankpage(request):
    if request.method == 'POST':
        status = request.POST['option']
        return render(request, 'dummybank/response.html', {'status': status})
    return render(request, 'dummybank/bankpage.html')

def response(request):
    status = request.POST['status']
    return render(request, 'dummybank/response.html', {'status': status})
