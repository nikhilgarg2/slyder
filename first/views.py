from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect
from .forms import *
from selenium import webdriver
import MySQLdb
#from .compile import compile1
from .models import *
from .scrol import scroll_first


def my_view(request):
    form = first_form()
    preset_form = websiteform()
    crawl_attri = crawl_attribute1()
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    searc=search1()
    website_map=website.objects.raw('SELECT * FROM `website`')
    #scro=scroll1()
    if request.method=="POST":
      if 'button3' in request.POST:
       form = first_form(request.POST or None)
       if form.is_valid():
          save_it=form.save(commit=False)
          save_it.save()
          #return HttpResponseRedirect('')         
          website_map=website.objects.raw('SELECT * FROM `website`')
         #return HttpResponseRedirect('')
      if 'button7' in request.POST:
        print request.POST['website_id']
    return render_to_response('signup.html',{'form': first_form,'posts':website_map},RequestContext(request))  
     


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


def crawl1(request):
    preset_form = websiteform()
    if request.method=="POST":        
        preset_form=websiteform(request.POST or None)
        #if preset_form.is_valid():
        if 'website_id' in request.POST:
                #print "hello"
                item_map=crawl_url.objects.filter(website_id__in=request.POST['website_id'])
                #print item_map
                return render_to_response('crawl.html',{'posts':item_map,'form':preset_form},RequestContext(request))
    return render_to_response('crawl.html',{'form':preset_form},RequestContext(request))
        