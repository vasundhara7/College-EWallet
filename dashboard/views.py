import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm , PasswordChangeForm
from django.contrib import messages
from django.views import generic
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.hashers import check_password

from dashboard.models import Profile
from .forms import UserRegisterForm, EditProfileForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.utils import timezone
from trans.models import Transact
from forms_builder.forms.models import Form



def index(request):
    return render(request, 'dashboard/homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')


            new_user = form.save(commit=False)
            new_user.is_active=False
            new_user.save()
            new_user.refresh_from_db()  # load the profile instance created by the signal
            new_user.save()
            role = form.cleaned_data.get('role')
            year = form.cleaned_data.get('year')
            phone_number = form.cleaned_data.get('phone_number')
            student_id=form.cleaned_data.get('student_id')
            #picture = form.cleaned_data.get('picture')

            profile = new_user.profile
            profile.role = role
            profile.year = year
            #profile.picture = picture
            profile.phone_number = phone_number
            profile.student_id=student_id
            profile.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your PayU account.'
            message = render_to_string('dashboard/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)).decode(),
                'token':account_activation_token.make_token(new_user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')


            #user = authenticate(username=new_user.username, password=raw_password)
            #login(request, user)

            # messages.success(request,f'Account created for {username}!')
            #return redirect('dashboard:accounts')
    else:
        form = UserRegisterForm()
    return render(request, 'dashboard/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed=True
        user.save()

        login(request, user)
        return redirect('dashboard:accounts')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')




@login_required(login_url='dashboard:login')
def accounts(request):
    user=request.user
    if user.username=='mess':
        return redirect('mess.index')
    elif user.username=='canteen':
        return redirect('canteen:vendor')
    elif user.username=='librarian':
        return  redirect('')
    else:

        return render(request, 'dashboard/account.html',{"forms": Form.objects.all()})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('dashboard:accounts')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'dashboard/homepage.html')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'dashboard/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST,instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('dashboard:accounts')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'dashboard/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def explore(request):
    return render(request, 'dashboard/explore.html', {"forms": Form.objects.all()})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard:accounts')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {
        'form': form
    })

def payments(request):
    all_users = Profile.objects.all()
    query=request.GET.get('q')
    if query:

        all_users=Profile.objects.filter(user__first_name__icontains=query)
        if not all_users:
            all_users=Profile.objects.filter(phone_number__icontains=query)
    return render(request, 'dashboard/payments.html', {'all_users':all_users})


def pay(request):
    receiver=request.GET.get('username')
    payee=User.objects.get(username=receiver)
    pay1=Profile.objects.get(user=payee)
    context={'receiver':payee,'receiver_profile':pay1}
    #pay2=Profile.phone_number(user=pay1)
    #print(pay2)
    return render(request, 'dashboard/pay.html',context)


def pay_a_friend(request):
    receiver=request.POST.get('username')
    passwd=request.POST.get('password')
    payee=User.objects.get(username=receiver)
    pay1=Profile.objects.get(user=payee)
    receiver_balance=pay1.balance
    amount=request.POST.get('amount')
    amount=int(amount)
    name=request.user
    f=name.first_name
    match=check_password(passwd,request.user.password)
    profile=Profile.objects.get(user=name)
    balance=profile.balance
    balance=int(balance)
    if match:
        if balance>amount:
            receiver_balance+=amount
            balance-=amount
            pay1.balance=receiver_balance
            pay1.save()
            profile.balance=balance
            profile.save()
            message1="successful"
            message2=""
            time=timezone.now()
            tr=Transact(Time=time,Amount=int(amount),Recipient=receiver)
            tr.save()
            mail_subject = 'Payment received'
            message = render_to_string('dashboard/pay_confirmation.html', {
                'receiver': payee.first_name,
                'sender':f,
                'amount':amount,
                'remaining_balance':receiver_balance,
            })
            to_email = payee.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()


        else:
            message1="unsuccessful"
            message2="Reason: Insufficient account balance"
    else:
        message1="unsuccessful"
        message2="Reason: Invalid password"
    context={'amount':amount,'receiver':payee,'receiver_profile':pay1, 'message1':message1, 'message2':message2}


    return render(request, 'dashboard/payprocess.html',context)
