from django.shortcuts import redirect, render, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 1.获取当前请求的url，设置白名单
        current_url = request.path_info
        for reg in settings.VALID_URL:
            if re.match(reg, current_url):
                return None
        # 2.获取当前用户session中的所有权限
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        print(permission_list)
        if not permission_list:
            return redirect('/login/')
        # 3.进行权限校验
        flag = False
        for item in permission_list:
            reg = "^%s$" % item.get('permissions__url')
            if re.match(reg, current_url):
                flag = True
                break

        if not flag:
            return HttpResponse('您无权访问，谢谢！')
