from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Laundrijess import views

urlpatterns = [
	path('admin/',admin.site.urls),
	path('', views.MainPage, name="first"),
	path('areyou',views.areyou, name="areyou"),
	path('equipments',views.equipments, name="equipments"),
	path('delivery',views.delivery, name="delivery"),
	path('payments',views.payments, name="payments"),
]