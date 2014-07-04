# forms.py
from django import forms
from .models import *
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
        model = crawl_url_attribute_css_sel
        exclude=[]
        
class prodid1(forms.ModelForm):
    class Meta:
        model=prodid
        exclude=[]
    #code

