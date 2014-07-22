from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect
from .forms import search1
from selenium import webdriver
import MySQLdb
from .models import *


def search123(request):
  searc=search1()
  if request.method=="POST":        
        searc=search1(request.POST or None)
        if searc.is_valid():
            if 'd_box' in request.POST:
                item_map=item.objects.raw('SELECT * FROM `item` WHERE `category_id`=%s', [request.POST['d_box']])
                lis=[]
                for e in (item_map):
                    lis.append(e.id)
                price_map=item_done.objects.filter(item_id__in=lis).order_by('item_id')
                return render_to_response('index.html',{'posts':price_map,'posts1':searc},RequestContext(request))
  return render_to_response('index.html',{'posts1':searc},RequestContext(request))
    