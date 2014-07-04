from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect
from .forms import *
from selenium import webdriver
import MySQLdb
from .compile import compile1
from .models import *

def my_view(request):
    form = first_form()
    preset_form = websiteform()
    crawl_attri = crawl_attribute1()
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    
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
        print 'x'
        crawl_attri=crawl_attribute1(request.POST)
        if crawl_attri.is_valid():
         save_it=crawl_attri.save(commit=False)
         save_it.save()
         return HttpResponseRedirect('')
      
      elif 'button5' in request.POST:
        crawl_css=crawl_url_attribute_css_sel1(request.POST or None)
        if crawl_css.is_valid():
         css=request.POST['css_sel']
         crawl_at=request.POST['crawl_attribute_id']
         crawl_id=request.POST['crawl_url_id']
         text1=request.POST['text_ar']
         prod=request.POST['prod_id']
         compile1(css,crawl_at, crawl_id, text1, prod)
         try3=crawl_url_attribute_css_sel.objects.filter(css_sel__contains=css)
         if len(try3)==0:
          save_it=crawl_css.save(commit=False)
          save_it.save()
         return HttpResponseRedirect('')
    
       
    return render_to_response('signup.html',{'preset_form': preset_form,'form':form,
            'crawl_attri':crawl_attri,'crawl_css':crawl_css,'prod':prod},RequestContext(request))



    