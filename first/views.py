from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect
from .forms import *
from selenium import webdriver
import MySQLdb
#from .compile import compile1
from .models import *
from .scrol import scroll_first
from .connect import *
from fuzzywuzzy import fuzz
import itertools

warning=0

def my_view(request):
    form = first_form()
    preset_form = websiteform()
    #crawl_attri = crawl_attribute1()
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    #scro=scroll1()
    searc=search1()
    website_map=website.objects.raw('SELECT * FROM `website`')
    global warning
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
            #global warning
            warning=request.POST['crawl_id']
            return HttpResponseRedirect('/details/')
      
      if 'button5' in request.POST:    
        x=request.POST['crawlid']
        item_try=final.objects.filter(crawl_id__exact=x)
        z=item_try[0]
        cat_query=cat.objects.filter(category__exact=z.cat)
        scroll_first(z.parent_css,z.prod_id,z.prod_attribute,z.name,z.mrp,z.sp,x,cat_query[0].id)
        return HttpResponseRedirect('')
      
      if 'crawl_all' in request.POST:
        sql="SELECT * FROM `crawl_url`"
        cursor.execute(sql)
        lis=cursor.fetchall()
        for e in range(len(lis)):
            x=lis[e][0]
            item_try=final.objects.filter(crawl_id__exact=x)
            z=item_try[0]
            cat_query=cat.objects.filter(category__exact=z.cat)
            scroll_first(z.parent_css,z.prod_id,z.prod_attribute,z.name,z.mrp,z.sp,x,cat_query[0].id)
        return HttpResponseRedirect('')
      
      if 'crawl_id1' in request.POST:
            #global warning
            warning=request.POST['crawl_id1']
            #print warning
            return HttpResponseRedirect('/details/')
    
    return render_to_response('signup.html',{'form': first_form,'posts':website_map},RequestContext(request))  
     



def search123(request):
  global itertool
  itertool=itertools.count()
  searc=search1()
  if request.method=="POST":        
        searc=search1(request.POST or None)
        if 'button7' in request.POST:
            if 'd_box' in request.POST and request.POST['d_box'] and not request.POST['name']:
                item_map=item.objects.raw('SELECT * FROM `item` WHERE `category_id`=%s', [request.POST['d_box']])
                lis=[]
                for e in (item_map):
                    lis.append(e.id)
                price_map=item_done.objects.filter(item_id__in=lis).order_by('item_id')
                return render(request,'index.html',{'posts':price_map,'posts1':searc,'itertools':itertool})
            
            else:
              x=request.POST['name']
              sql="SELECT * FROM `item`"
              cursor.execute(sql)
              query=cursor.fetchall()
              lis=[]
              for e in range(len(query)):
                    y=str(query[e][1])
                    rat=fuzz.token_set_ratio(x,y)
                    if rat >= 75:
                        lis.append(query[e][0])
              price_map=item_done.objects.filter(item_id__in=lis).order_by('item_id','site_price')
              return render(request,'index.html',{'posts':price_map,'posts1':searc,'itertools':itertool})
  
  return render_to_response('index.html',{'posts1':searc},RequestContext(request))


def add_details(request):
    crawl_css=crawl_url_attribute_css_sel1()
    prod=prodid1()
    #print warning
    x=crawl_url.objects.get(crawl_id__exact=warning)
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
                #print request.POST['crawl_id']
                #print len(try3)
                if len(try3)==0:
                 save_it=crawl_css.save(commit=False)
                 save_it.save()
                scroll_first(css,prod, proda, naam, maxrp, sellp, crawl,category)
                return HttpResponseRedirect('')    
    return render(request,'add.html',{'yd':x,'post':scro,'prod1':prod,'crawl':crawl_css})

def login1(request):
    log=login()
    if request.method=="POST":
        if 'login_but' in request.POST:
            log=login(request.POST or None)
            password = request.POST.get('password', False);
            sql="SELECT `id` FROM `log_id` WHERE `name`=%s and `password`=%s"
            values=(request.POST['name'], password)
            cursor.execute(sql,values)
            final=cursor.fetchall()
            if len(final)!=0:
                return HttpResponseRedirect('/blog/')
    return render(request,'login.html',{'log':log})        