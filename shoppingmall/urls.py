from django.conf.urls import include, url
from django.contrib import admin
from shoppingmall_app.views import account  as ac
from  shoppingmall_app.forms import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'shoppingmall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form1/$',ac.form1),
    url(r'^form2/$',ac.form2),
    url(r'^form3/$',ac.form3),
]
