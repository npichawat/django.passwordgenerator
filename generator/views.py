from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')


def password(request):


	characters = list('abcdefghijklmnoqtuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend('ABCDEFGHIJKLMNOQTUVWXYZ')

	if request.GET.get('Special characters'):
		characters.extend('!@#$%^&*_+')

	if request.GET.get('Numbers'):
		characters.extend('0123456789')


	length = int(request.GET.get('length'))

	thepassword = ''
	for x in range(length):
		thepassword += random.choice(characters)



	return render(request, 'generator/password.html', {'password':thepassword})