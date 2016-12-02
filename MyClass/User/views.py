# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from User.models import *
from Homework.models import *
# Create your views here.

def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

def login(request):
    if request.method == 'POST':
        number = request.POST.get('number', None)
        password = request.POST.get('password', None)
        password = encry_password(password)
        user = User.objects.filter(number = number, password = password)
        info = {}
        if number != None and password != None and len(user) > 0:
            request.session['number'] = user[0].number
            request.session['name'] = user[0].name
            info['state'] = True
            info['url'] = reverse('index')
        else :
            info['state'] = False
            info['url'] = reverse('login')
        return JsonResponse(info)
    else :
        return render(request, 'User/login.html')


def logout(request):
    if request.session.get('number', None):
        del request.session['number']
    return HttpResponseRedirect(reverse('login'))


def index(request):
    if request.session.get('number', None):
        user = User.objects.get(number = request.session['number'])
        info = {'user': user}
        return render(request, 'User/index.html',info)
    else :
        return HttpResponseRedirect(reverse('login'))

def change_avatar(request):
    user = User.objects.get(name = request.session['name'])
    if request.method == 'POST':
        avatar = request.FILES['avatar']
        print '+++++',avatar
        user.avatar = avatar;
        user.save()
        return HttpResponseRedirect(reverse('index'))
    else :
        return HttpResponseRedirect(reverse('index'))

