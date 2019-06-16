from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from dashboard.models import Profile
import json
import re
rec_name = ""
def index(request):
    return render(request, 'chat/index.html')

@login_required(login_url='dashboard:login')
def room(request, room_name):
    print(room_name)
    print("printed roomname")
    r_n=room_name
    print("userID" + str(request.user.id))
    r_n=re.sub(str(request.user.id),"",r_n,1);
    print(r_n)
    r_n=int(r_n)
    if(Profile.objects.filter(user_id=r_n).count()>0):
        rec = Profile.objects.get(user_id=r_n)
        sen = Profile.objects.get(user_id=request.user.id)
        print(request.user.username)
        a1= Profile.objects.all()
        ul=[]
        for a in a1:
            if (str(a.user) != str(request.user.username)):
                ul.append(a)
        rezname=str(rec.user)
        print(mark_safe(json.dumps(rezname)))
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': mark_safe(json.dumps(request.user.username)),
            'uzername': str(request.user.username),
            'rezname':mark_safe(json.dumps(rezname)),
            'userid': mark_safe(json.dumps(request.user.id )),
            'userlist':ul,
            'rec':rec,
            'recname':str(rec.user),
            'sen':sen,


        })
    else:
        return HttpResponse("webpage not found")
