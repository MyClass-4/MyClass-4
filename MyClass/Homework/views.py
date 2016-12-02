# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import os
from User.models import *
from Homework.models import *
from MyClass.settings import BASE_DIR, MEDIA_ROOT
# Create your views here.

def upload_homework(request):
    if request.method == 'GET':
        course_list = Course.objects.all()
        # print course_list
        homework_type_list = HomeworkType.objects.all()
        info = {'course_list':course_list, 'homework_type_list': homework_type_list}
        return render(request, 'Homework/upload_homework.html', info)
    else: # POST
        print 'POST =>>>'
        course_name = request.POST.get('course_name', None)
        homework_name = request.POST.get('homework_name', None)
        homework_type = HomeworkType.objects.filter(name = homework_name)
        if homework_type.count() > 0:
            homework_type = homework_type[0]
        else :
            homework_type = None
        course = None
        if course_name != None:
            course = Course.objects.get(course_name = course_name)
        homework_file = request.FILES.get('homework', None)
        user = User.objects.get(number = request.session['number'])
        homework, not_exist = Homework.objects.get_or_create(author = user, homework_type = homework_type)
        info = {}
        if not_exist:
            homework.source = homework_file
            info['state'] = True
            info['message'] = '文件上传成功'
        else: # 已经上传过改作业
            print os.path.join(MEDIA_ROOT, homework.source.name)
            if os.path.isfile(os.path.join(MEDIA_ROOT, homework.source.name).replace('\\', '/')):
                print 'upload file <', homework_file.name , '> success!'
                os.remove(os.path.join(MEDIA_ROOT, homework.source.name).replace('\\', '/'))
            homework.source = homework_file
            info['state'] = True
            info['message'] = '文件覆盖成功'
        homework.save()
        return HttpResponse('upload_success');

def statistic(request):
    return HttpResponse('under constructions')

def homework_notice(request):
    homeworkType_list = HomeworkType.objects.all()
    # print homeworkType_list
    info = {'homeworkType_list': homeworkType_list}
    return render(request, 'Homework/homework_notice.html', info)

def achievement(request):
    homeworkType_list = HomeworkType.objects.all().order_by('course__course_name', 'name')
    homework_state_list = []
    for homeworkType in homeworkType_list:
        user = User.objects.get(name = request.session['name'])
        if len(Homework.objects.filter(homework_type = homeworkType, author = user)) > 0:
            homework_state_list.append([homeworkType, True])
        else:
            homework_state_list.append([homeworkType, False])
    info = {'homework_state_list': homework_state_list}
    return render(request, 'Homework/achievement.html', info)
