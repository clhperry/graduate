from django.shortcuts import render
from django.http import HttpResponse
from core.models import Course 
def home(request):
	return render(request, 'home.html')

def acct(request):
 	courses = Course.objects.all()
 	return render(request, 'acct.html', {'courses': courses})

def ecof(request):
 	courses = Course.objects.all()
 	return render(request, 'ecof.html', {'courses': courses})

def econ(request):
 	courses = Course.objects.all()
 	return render(request, 'econ.html', {'courses': courses})

def fina(request):
 	courses = Course.objects.all()
 	return render(request, 'fina.html', {'courses': courses})

def gbus(request):
 	courses = Course.objects.all()
 	return render(request, 'gbus.html', {'courses': courses})

def bbais(request):
 	courses = Course.objects.all()
 	return render(request, 'is.html', {'courses': courses})

def mark(request):
 	courses = Course.objects.all()
 	return render(request, 'mark.html', {'courses': courses})

def mgmt(request):
 	courses = Course.objects.all()
 	return render(request, 'mgmt.html', {'courses': courses})

def om(request):
 	courses = Course.objects.all()
 	return render(request, 'om.html', {'courses': courses})

def qfin(request):
 	courses = Course.objects.all()
 	return render(request, 'qfin.html', {'courses': courses})