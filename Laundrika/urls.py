from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Laundrijess import views

urlpatterns = [
	path('admin/',admin.site.urls),
	path('', views.AreYou, name="first"),
	path('areyou',views.MainPage, name="second"),
	path('equipments',views.Equipments, name="third"),
	path('delivery',views.Delivery, name="forth"),
	path('payments/',views.Payments, name="fifth"),
]