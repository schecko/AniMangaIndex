
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('deleteContent/<int:contentID>/', views.deleteContent, name = 'delete content'),
	path('nextFavorites/', views.nextFavorites, name = 'next favorites'),
	path('addFavorite/<int:contentID>/', views.addFavorite, name = 'add favorite'),
	path('content/<int:contentID>/', views.contentDetail, name = 'content detail'),
	path('creator/<int:creatorID>/', views.creatorDetail, name = 'creator detail'),
	path('userDetail/', views.userDetail, name = 'user detail'),
	path('genre/', views.genreDetail, name = 'genre detail'),
	path('selection/', views.selectionDetail, name = 'selection detail'),
	path('nested/', views.nestedDetail, name = 'nested detail'),
	path('create/', views.createDetail, name = 'create detail'),
	path('division/', views.divisionDetail, name = 'division detail')
]
