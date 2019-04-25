from django.shortcuts import render,redirect
from rbac.models import UserInfo,Role,Permission
from django.conf import settings
# Create your views here.
def login(request):
    # 校验用户是否合法
    if request.method == 'GET':
        return render(request,'login.html')

    # 1. 获取提交的用户名和密码
    user = request.POST.get('username')
    pwd = request.POST.get('pwd')

    # 2. 检验用户是否合法
    obj = UserInfo.objects.filter(name=user,password=pwd).first()
    if not obj:
        return render(request, 'login.html',{'msg':'用户名或密码错误'})

    # 3.将用户信息和所对应角色的权限信息放到session中
    permission_list = obj.roles.filter(permissions__url__isnull=False).values('permissions__url').distinct()
    # print(permission_list)
    # print(list(permission_list))
    request.session['user_info'] = {'id':obj.id,'name':obj.name}
    request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)



    return redirect('/customer/list/')