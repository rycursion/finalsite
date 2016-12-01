from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from . import cart
from .models import Product

def home(request):
	try:
		cart.c.lst.append(0)
		cart.c.lst.remove(0)
	except:
		cart.create()
	games=Product.objects.order_by('id')
	return render(request, 'gcom/home.html')

def list(request):
	product_list = Product.objects.order_by('-id')
	product_dictionary = {"Action":[],"Sports":[],"Strategy":[]}
	for i in product_list:
		product_dictionary[i.genre].append(i.id)
	return render(request, "gcom/list.html", {"p_dict" : product_dictionary, "p_list" : product_list})

def product(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, "gcom/gamepage.html", {"product": product})

def aproduct(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	cart.c.add(product.id)
	return render(request, "gcom/gamepage.html", {"product": product})	

def xcart(request):
	product_list = cart.c.lst
	t_price=0
	p_list=[]
	for i in range(len(product_list)):
		p_list.append(get_object_or_404(Product, pk=product_list[i]))
		p=get_object_or_404(Product, pk=product_list[i])
		t_price+=p.price
	return render(request, "gcom/cart.html", {"p_list" : p_list, "t_price":t_price })

def u_cart(request, product_id):
	product_id=int(product_id)
	if product_id!=0:
		cart.c.remove(product_id)
		product_list = cart.c.lst
		p_list=[]
		t_price=0
		for i in range(len(product_list)):
			p_list.append(get_object_or_404(Product, pk=product_list[i]))
			p=get_object_or_404(Product, pk=product_list[i])
			t_price+=p.price
		if p_list:
			return render(request, "gcom/cart.html", {"p_list" : p_list, "t_price":t_price})
		else:
			return render(request, "gcom/cart.html", {"p_list" : [], "t_price": 0})
	else:
		cart.c.empty_cart()
		return HttpResponseRedirect(reverse('gcom:home'))

def contact(request):
    
    return render(request, 'gcom/contact page.html')
