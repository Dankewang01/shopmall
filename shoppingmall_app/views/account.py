from django.shortcuts import render,HttpResponse
from shoppingmall_app.forms import *
from shoppingmall_app.models import *

def form1(request):
    if request.method=="POST":  #这里POST一定要大写
        #通常获取请求信息
        #request.POST.get("user",None)
        #request.POST.get("pwd",None)
        #获取请求内容，做验证
        f = Form1(request.POST)  #request.POST：将接收到的数据通过Form1验证
        if f.is_valid():  #验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
            print(f.cleaned_data)  #cleaned_data类型是字典，里面是提交成功后的信息
        else:  #错误信息包含是否为空，或者符合正则表达式的规则
            print(type(f.errors),f.errors)  #errors类型是ErrorDict，里面是ul，li标签
            return render(request,"shoppingmall/form1.html",{"error":f.errors})
    return render(request,"shoppingmall/form1.html")


#upgrade_build

def form2(request):
    if request.method == "POST":
        f = Form1(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
        else:
            return render(request,"shoppingmall/form2.html",{"error":f.errors,"form":f})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        f = Form1()
        return render(request,"shoppingmall/form2.html",{"form":f})
    return render(request,"shoppingmall/form2.html")

# def test(req):
#     BookType.objects.create(caption='技术')
#     BookType.objects.create(caption='文学')
#     BookType.objects.create(caption='动漫')
#     BookType.objects.create(caption='男人装')
#     return HttpResponse("ok")


def form3(request):
    if request.method == "POST":
        f = Form3(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
        else:
            return render(request,"shoppingmall/form3.html",{"error":f.errors,"form":f})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        f = Form3()
        return render(request,"shoppingmall/form3.html",{"form":f})
    return render(request,"shoppingmall/form3.html")