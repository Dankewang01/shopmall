

# forms 里面的字段限制


required：是否可以为空。required=True 不可以为空，required=False 可以为空
max_length=4 最多4个值，超过不会显示
min_length=2 至少两个值，少于两个会返回提示信息
error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'}  自定义错误信息，invalid 是格式错误
widget=forms.TextInput(attrs={'class': 'c1'}) 给自动生成的input标签自定义class属性
widget=forms.Textarea()  生成Textarea标签。widget默认生成input标签


# form 格式

<form action="/form3/" method="POST">
        <div class="input-group"> (input-group自动生成输入格式)
{#          接收后台传过来的form对象，自动生成input标签#}
            姓名：{{ form.user }}
{#          从后台传过来的error是字典，直接{{ error.user.0 }}呈现错误信息#}
{#          如果后台返回了错误信息，将错误信息放入span标签，在页面显示，否则不显示#}
            {% if error.user.0 %}
            <span>{{ error.user.0 }}</span>
            {% endif %}
        </div>