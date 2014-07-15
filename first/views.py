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
    searc=search1()
    prod=prodid1()
    scro=scroll1()
    if request.method=="POST":
      if 'button2' in request.POST:
        preset_form=websiteform(request.POST or None)
        if preset_form.is_valid:
         save_it=preset_form.save(commit=False)
         save_it.save()
         return HttpResponseRedirect('')
      
      elif 'button1' in request.POST :
        prod=prodid1(request.POST or None)
        if prod.is_valid():
         save_it=prod.save(commit=False)
         save_it.save()
         return HttpResponseRedirect('')
      
      elif 'button3' in request.POST:
         form = first_form(request.POST or None)
         if form.is_valid():
          save_it=form.save(commit=False)
          save_it.save()
          return HttpResponseRedirect('')         
      
      elif 'button4' in request.POST:
        #print 'x'
        crawl_attri=crawl_attribute1(request.POST)
        if crawl_attri.is_valid():
         save_it=crawl_attri.save(commit=False)
         save_it.save()
         return HttpResponseRedirect('')
      
      elif 'button5' in request.POST:
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
         save_it=crawl_css.save(commit=False)
         save_it.save()
         scroll_first(css,prod, proda, naam, maxrp, sellp, crawl,category)
         return HttpResponseRedirect('')
     
     
      elif 'button6' in request.POST:
        scro=scroll1(request.POST or None)
        if scro.is_valid():
            save_it=scro.save(commit=False)
            save_it.save()
            return HttpResponseRedirect('') 
     
      elif 'button7' in request.POST:
        searc=search1(request.POST or None)
        if searc.is_valid():
            if 'd_box' in request.POST:
                price_map=item_done.objects.raw('SELECT * FROM `item_done` WHERE `cat_id`=%s', [request.POST['d_box']])
                template_data={'posts':price_map}
                return render_to_response('index.html', template_data,RequestContext(request))
            #return HttpResponseRedirect('')
       
    return render_to_response('signup.html',{'preset_form': preset_form,'form':form,
            'crawl_attri':crawl_attri,'crawl_css':crawl_css,'prod':prod,'scro':scro,'searc':searc},RequestContext(request))



    