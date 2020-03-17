from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('zapa/', views.zapa, name = 'zapa'),
	path('onas/', views.onas, name = 'onas'),
]