from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Laundrijess import views

urlpatterns = [
	path('admin/',admin.site.urls),
	path('', views.MainPage, name="first"),
	path('areyou',views.AreYou, name="second"),
	path('equipments',views.Equipments, name="third"),
	path('delivery',views.Delivery, name="forth"),
	path('payment',views.Payment, name="fifth"),
]