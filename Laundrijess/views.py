from django.shortcuts import render, redirect
import random

def MainPage(request):

	return render(request, 'mainpage.html')

#remove parenthesis in ref number
def create_new_ref_number():
                not_unique = True
                while not_unique:
                    unique_ref = random.randint(1000000000, 9999999999)
                    if not Transaction.objects.filter(Referrence_Number=unique_ref):
                        not_unique = False
                return str(unique_ref)

