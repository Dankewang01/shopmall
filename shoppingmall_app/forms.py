from django import forms

class Form1(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()


from django import forms
from shoppingmall_app import models


class Form3(forms.Form):
    user = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'c1'}),
        error_messages={'required': '用户名不能为空'}, )
    pwd = forms.CharField(max_length=4, min_length=2, required=True)
    email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})

    memo = forms.CharField(
        widget=forms.Textarea()
    )

    # 直接写数据
    # user_type_choice = (
    #     (0, '普通用户'),
    #     (1, '高级用户'),
    # )
    # 通过BookType表查询信息，values_list拿到的是元组。id作为value显示，caption作为text在页面显示
    # user_type_choice = models.BookType.objects.values_list('id', 'caption')
    # book_type = forms.CharField(
    #     widget=forms.widgets.Select(choices=user_type_choice, attrs={'class': "form-control"}))

    # 写上以下代码就不用担心数据库添加了数据而不能及时获取了
    def __init__(self, *args, **kwargs):
        # 每次创建Form3对象时执行init方法
        super(Form3, self).__init__(*args, **kwargs)

        self.fields['book_type'] = forms.CharField(
            widget=forms.widgets.Select(choices=models.BookType.objects.values_list('id', 'caption'),
                                        attrs={'class': "form-control"}))


import re
from django import forms
from django.core.exceptions import ValidationError

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class PublishForm(forms.Form):

    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )

    user_type = forms.IntegerField(widget=forms.widgets.Select(choices=user_type_choice,
                                                                  attrs={'class': "form-control"}))

    title = forms.CharField(max_length=20,
                            min_length=5,
                            error_messages={'required': u'标题不能为空',
                                            'min_length': u'标题最少为5个字符',
                                            'max_length': u'标题最多为20个字符'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'标题5-20个字符'}))

    memo = forms.CharField(required=False,
                           max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))

    phone = forms.CharField(validators=[mobile_validate, ],
                            error_messages={'required': u'手机不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'手机号码'}))

    email = forms.EmailField(required=False,
                            error_messages={'required': u'邮箱不能为空','invalid': u'邮箱格式错误'},
                            widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))

