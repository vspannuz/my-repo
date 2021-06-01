from django.conf.urls import url
from first import views

app_name = 'first'

urlpatterns = [
url(r'^relative/$',views.relative,name='relative'),
url(r'^relative/others/$',views.others,name='others'),
url(r'^others/$',views.others,name='others')
]
