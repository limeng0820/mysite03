from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from polls import models  # 导入models文件
# Create your views here.

def index(request):
    pass
    return render(request, 'polls/index.html')


def login(request):
    pass
    return render(request, 'polls/login.html')

def register(request):
    pass
    return render(request, 'polls/register.html')


def logout(request):
    pass
    return redirect("/index/")