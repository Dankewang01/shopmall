
from django.db import models
import time
# Create your models here.
class Author(models.Model):
    """
    作者
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class BookType(models.Model):
    """
    图书类型
    """
    caption = models.CharField(max_length=64)

    def __str__(self):
        return self.caption


class Book(models.Model):
    """
    图书
    """
    name = models.CharField(max_length=64)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    pubdate = models.DateField()

    authors = models.ManyToManyField(Author)
    book_type = models.ForeignKey(BookType)



    def __str__(self):
       return self.name

    def getAuthorName(self):
        return self.Author.name

    def curTime(self):
        return time.time()

    curTime.short_description = "当前时间"
    curTime.admin_order_feild = "name"  # 设置为以name为准，对函数进行排序










#class BookType(models.Model):