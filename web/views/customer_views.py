from django.shortcuts import render, redirect
from web.models import Customer, Payment
from web.forms.customer import CustomerForm


# Create your views here.
# 用户展示
def customer_list(request):
    customer_list = Customer.objects.all()
    return render(request, 'customer_list.html', {'customer_list': customer_list})


# 增加用户
def customer_add(request):
    # get请求
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'customer_add.html', {'form': form})

    # post请求
    form = CustomerForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/customer/list')
    return render(request, 'customer_add.html', {'form': form})


# 编辑客户
def customer_edit(request, cid):
    obj = Customer.objects.get(id=cid)
    if request.method == 'GET':
        form = CustomerForm(instance=obj)
        return render(request, 'customer_edit.html', {'form': form})

    form = CustomerForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()

        return redirect('/customer/list/')

    return render(request, 'customer_edit.html', {'form': form})

# 删除客户
def customer_del(request,cid):
    Customer.objects.filter(id=cid).delete()
    return redirect('/customer/list/')
