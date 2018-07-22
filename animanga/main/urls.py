
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
	path('', views.index, name='index'),
	path('content/<int:contentID>/', views.contentDetail, name = 'content detail'),
	path('creator/<int:creatorID>/', views.creatorDetail, name = 'creator detail'),
]