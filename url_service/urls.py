from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<short_url>[0-9A-Za-z]+)/$', views.redirect, name='redirect'),
    url(r'^(?P<short_url>[0-9A-Za-z]+)/inflate/$', views.inflate, name='inflate'),
]
