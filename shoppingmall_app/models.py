
from django.db import models

# Create your models here.
class Author(models.Model):
    """
    作者
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class BookType(models.Model):
    """
    图书类型
    """
    caption = models.CharField(max_length=64)

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