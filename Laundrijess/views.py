from django.shortcuts import render, redirect

def MainPage(request):

	return render(request, 'mainpage.html')

