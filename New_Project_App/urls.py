from django.urls import re_path as url
from . import views

urlpatterns=[
 url(r'^$',views.main,name='main'),
 url(r'^aboutUs',views.aboutUs,name='aboutUs'),
 url(r'^signup', views.main, name = 'sign up'),
 url(r'^login', views.main, name = 'login'),
 url(r'^logout', views.main, name = 'logout'),
]