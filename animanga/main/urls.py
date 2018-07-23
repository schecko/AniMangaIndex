
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('content/<int:contentID>/', views.contentDetail, name = 'content detail'),
	path('creator/<int:creatorID>/', views.creatorDetail, name = 'creator detail'),
]