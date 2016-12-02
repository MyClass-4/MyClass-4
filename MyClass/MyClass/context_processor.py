# -*- coding:utf-8 -*-
from Homework.models import *
from User.models import *
from Myclass.wigi import *

def page_head(request):
    number = request.session.get('number', None)
    info = {}
    if number != None:
        user = User.objects.get(number = number)
        info['user':user]
    info['request'] = request;
    return info
