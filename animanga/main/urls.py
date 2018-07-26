
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('deleteContent/<int:contentID>/', views.deleteContent, name = 'delete content'),
	path('nextFavorites/', views.nextFavorites, name = 'next favorites'),
	path('content/<int:contentID>/', views.contentDetail, name = 'content detail'),
	path('creator/<int:creatorID>/', views.creatorDetail, name = 'creator detail'),
	path('genre/', views.genreDetail, name = 'genre detail'),
	path('projection/', views.projectionDetail, name = 'projection detail'),
        path('selection/', views.selectionDetail, name = 'selection detail'),
	path('nested/', views.nestedDetail, name = 'nested detail'),
	path('create/', views.createDetail, name = 'create detail'),
        path('division/', views.divisionDetail, name = 'division detail')
]
