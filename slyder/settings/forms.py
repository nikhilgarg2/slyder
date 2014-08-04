# forms.py
from django import forms
from .models import *

from .models import search
#from .models import website
       
class first_form(forms.ModelForm):
    class Meta:
        model=website
        exclude=[]
        #code
    
        
class websiteform(forms.ModelForm):
    class Meta:
        model=crawl_url
        exclude=[]

class crawl_attribute1(forms.ModelForm):
    class Meta:
        model=crawl_attribute
        exclude=[]
    #code

class crawl_url_attribute_css_sel1(forms.ModelForm):
    class Meta:
        model = final
        exclude=[]
        
class prodid1(forms.ModelForm):
    class Meta:
        model=cat
        exclude=[]

class scroll1(forms.ModelForm):
    class Meta:
        model=scroll
        exclude=[]

class search1(forms.ModelForm):
    class Meta:
        model=search
        exclude=[]

class login(forms.ModelForm):
    class Meta:
        model=log_id
        exclude=[]
    
    #code
