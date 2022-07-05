from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'projects/store.html', context)

def cart(request):
	context = {}
	return render(request, 'projects/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'projects/checkout.html', context)