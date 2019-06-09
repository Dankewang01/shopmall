from django.contrib import admin
from shoppingmall_app.models import Author, Book, BookType
# Register your models here.

admin.site.site_header = "失恋博物馆"
admin.site.site_title = "治愈空间"
admin.site.index_title = "有你的回忆"

class BookAdmin(admin.ModelAdmin):
   # fields = ['name', 'pubdate']  # 只显示name price 字段信息
    list_per_page = 2
    actions_on_buttom = True
    actions_on_top = False
    list_display = ["name", "curTime", "getAuthorName"]  # 显示数据库字段
    search_fields = ["name"]   #搜索选框，搜索NAME字段

  

admin.site.register(Book,BookAdmin)


'''
#@admin.register(Book) #注册装饰器写法
class BookAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_buttom = True
    actions_on_top = False
    list_display =[ "name", "curTime", "getAuthorName"]#显示数据库字段
    search_fields = ["name"]  #搜索选框，搜索NAME字段

    fields = ['name' , 'pubdate']#只显示name price 字段信息

    #分组显示
    fieldssets=(
        ('基本信息',{'fields':['name',]}),
        ('其他信息',{'fields':['price',]}),
    )

admin.site.register(Book,BookAdmin)
'''

#@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]  # 显示数据库字段
    search_fields = ["name"]  # 搜索选框，搜索NAME字段

admin.site.register(Author, AuthorAdmin)


#@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ["caption"]  # 显示数据库字段
    search_fields = ["caption"]  # 搜索选框，搜索NAME字段
    list_per_age = 2

admin.site.register(BookType,BookTypeAdmin)





