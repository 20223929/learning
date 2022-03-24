from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单信息
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，在重定向主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # 调用登录函数
            login(request, authenticated_user)
            # 重定向到主页
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
