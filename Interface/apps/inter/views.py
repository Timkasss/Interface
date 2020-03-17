from django.shortcuts import render

def index(request):
	return render(request, 'inter/index.html')

def zapa(request):
	return render(request, 'inter/zapa.html')

def onas(request):
	return render(request, 'inter/onas.html')

