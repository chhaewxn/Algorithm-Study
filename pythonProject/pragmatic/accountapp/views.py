from django.http import HttpResponse # 자동 모듈 생성
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return render(request, 'accountapp/hello_world.html')