from django.shortcuts import render
from cmdb import models
# from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('Hello, big world!')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        # 添加到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库中读取
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html", {'data':user_list})