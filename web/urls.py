"""low_permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from web.views import login_views,customer_views,payment_views,token_test

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    # 登录
    url(r'^login/$', login_views.login),
    # 客户信息
    url(r'^customer/list/$', customer_views.customer_list),
    url(r'^customer/add/$', customer_views.customer_add),
    url(r'^customer/edit/(?P<cid>\d+)/$', customer_views.customer_edit),
    url(r'^customer/del/(?P<cid>\d+)/$', customer_views.customer_del),



    # 付款信息
    url(r'^payment/list/$', payment_views.payment_list),
    url(r'^payment/add/$', payment_views.payment_add),
    url(r'^payment/edit/(?P<pid>\d+)/$', payment_views.payment_edit),
    url(r'^payment/del/(?P<pid>\d+)/$', payment_views.payment_del),


    url(r'^login_test/$', token_test.LoginView.as_view()),

]
