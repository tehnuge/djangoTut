import json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Produce, Transaction
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from mysite.views import get_creator_items

def index(request):
	#if new item submitted, save new item
	if request.method =="POST" and request.POST.get('action') == 'new':
		item = request.POST['item']
		qty = request.POST['qty']
		creator = request.user
		newItem = Produce(creator = creator, produce_text = item, quantity = qty)
		newItem.save()

	context = get_creator_items(request)

	return render(request, 'index.html', context)

#editing items
def modify_item(request):
	if request.is_ajax() and request.POST.get('action') == 'save':
		print request.POST
		itemid = request.POST.get('id')
		newText = request.POST.get('newText')
		newAmount = request.POST.get('newAmount')
		quantity = request.POST.get('quantity')
		i = Produce.objects.select_for_update().get(id=itemid)	
		if newText is not i.produce_text:
			i.produce_text = newText
		if newAmount is not i.quantity:
			i.quantity = newAmount
		i.save()
	if request.is_ajax() and request.POST.get('action') == 'destroy':
		itemid = request.POST.get('id')
		Produce.objects.filter(id=itemid).delete()
	if request.POST.get('action') == 'buy':
		print request.POST
		itemid = request.POST.get('id')
		item = request.POST.get('name')
		seller = Produce.objects.get(id=itemid).creator
		buyer = request.user
		buyAmount = request.POST.get('buyAmount')
		newTrans = Transaction(buyer=buyer, seller=seller, item=item, amount=buyAmount)
		newTrans.save()
		#print 'number:', number
	context = get_creator_items(request)
	return render(request, 'index.html', context)


#NOT BEING USED BY profile.jsx anymore, DELETE??? API for updating the 'inventory' global variable
#I dont need to alter the 'inventory' variable since react is taking care of how it looks
'''
def update_items(request):
	context = get_creator_items(request)
	print "is ajax!!!"
	return HttpResponse(context['inventory'], content_type="application/json")
'''