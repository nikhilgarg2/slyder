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
    #crawl_attri = crawl_attribute1()
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    #scro=scroll1()
    searc=search1()
    website_map=website.objects.raw('SELECT * FROM `website`')
    if request.method=="POST":
      if 'button3' in request.POST:
       form = first_form(request.POST or None)
       if form.is_valid():
          save_it=form.save(commit=False)
          save_it.save()
          website_map=website.objects.raw('SELECT * FROM `website`')
      if 'button7' in request.POST:
        item_map=crawl_url.objects.filter(website_id__in=request.POST['website_id'])
        return render_to_response('crawl.html',{'posts2':item_map,'form1':preset_form},RequestContext(request))
      if 'button4' in request.POST:
          preset_form = websiteform(request.POST or None)
          if  preset_form.is_valid():
            save_it=preset_form.save(commit=False)
            save_it.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/details/')
      if 'button5' in request.POST:    
        print "dimaag kharav"            
    
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


def add_details(request):
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    scro=scroll1()
    if request.method=="POST":
        if 'button1' in request.POST:
            scro=scroll1(request.POST or None)
            if scro.is_valid():
             save_it=scro.save(commit=False)
             save_it.save()
             return HttpResponseRedirect('')
        elif 'button2' in request.POST:
            prod=prodid1(request.POST or None)
            if prod.is_valid():
                 save_it=prod.save(commit=False)
                 save_it.save()
                 return HttpResponseRedirect('')
        elif 'button3' in request.POST:
            crawl_css=crawl_url_attribute_css_sel1(request.POST or None)
            if crawl_css.is_valid():
                css=request.POST['parent_css']
                prod=request.POST['prod_id']
                proda=request.POST['prod_attribute']
                naam=request.POST['name']
                maxrp=request.POST['mrp']
                sellp=request.POST['sp']
                crawl=request.POST['crawl_id']
                category=request.POST['cat']
                try3=final.objects.filter(crawl_id__exact=request.POST['crawl_id'])
                print request.POST['crawl_id']
                print len(try3)
                if len(try3)==0:
                 save_it=crawl_css.save(commit=False)
                 save_it.save()
                scroll_first(css,prod, proda, naam, maxrp, sellp, crawl,category)
                return HttpResponseRedirect('')    
    return render(request,'add.html',{'post':scro,'prod1':prod,'crawl':crawl_css})