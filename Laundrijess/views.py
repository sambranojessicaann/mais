from django.shortcuts import render, redirect
import random

def MainPage(request):

	return render(request, 'mainpage.html')

def AreYou(request):

	return render(request, 'areyou.html')

def Equipments(request):

	return render(request, 'equipments.html')

def Delivery(request):

	return render(request, 'delivery.html')

def Payment(request):

	return render(request, 'Payment.html')

