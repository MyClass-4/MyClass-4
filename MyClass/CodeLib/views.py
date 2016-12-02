# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from MyClass.settings import BASE_DIR, MEDIA_ROOT
import os
# Create your views here.

def coding(request):
	if request.method == 'POST':
		textCode = request.POST.get('testCode', "")
		# file = open(os.path.join(BASE_DIR, 'commonStatic/html/demo.html').replace('\\', '/'), "w")
		# file.write(textCode.encode('utf-8'));
		# file.close()
		return HttpResponse(textCode)

	else:
		return render(request, 'CodeLib/coding.html')		
