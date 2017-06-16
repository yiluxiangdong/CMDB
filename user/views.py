#coding:utf-8
from django.shortcuts import render_to_response,redirect,HttpResponseRedirect,render
from .models import *
import hashlib
# Create your views here.

def hash_passwd(password):
    hash_md5 = hashlib.md5()
    if isinstance(password,unicode):
        hash_md5.update(password.encode('utf-8'))
    passwd = hash_md5.hexdigest()
    return passwd

def  userVaild(username):
    userList = User.objects.filter(users = username)
    if userList:
        return True
    else:
        return False

def index(request):
    username = request.COOKIES.get('user','None')
    if request.session.get('userdata',''):
        return render_to_response('index.html',locals())
    else:
        return HttpResponseRedirect('/user/login')
def  login(request):
    if request.method=='POST' and request.POST:
        name = request.POST['name']
        passwd = hash_passwd(request.POST['passwd'])
        if userVaild(name):
            data = User.objects.get(users = name)
            pwd = data.passwd
            if passwd==pwd:
                response = HttpResponseRedirect('/user/index')
                response.set_cookie('user',name)
                request.session['userdata']=name
                return response
            else:
                return redirect('/user/login')
        else:
            return redirect('/user/login')
    else:
        return render_to_response('signin.html', locals())

def register(request):
    username = request.POST.get('user')
    if  request.method == 'POST' and request.POST:
        # if User.objects.filter(users=username):
        if userVaild(username):
            return render(request, '404.html')
        else:
            u = User()
            u.users = request.POST['user']
            u.passwd = hash_passwd(request.POST['passwd'])
            u.name = request.POST['name']
            u.city = request.POST['city']
            u.email = request.POST['email']
            u.phone = request.POST['phone']
            u.save()
            return redirect('/user/login')
    else:
        return render_to_response('signup.html',locals())