from django.contrib import admin
from .models import *

class SignUpAdmin(admin.ModelAdmin):
	 class Meta:
	 	model=website

class try_123(admin.ModelAdmin):
    class Meta:
        model=crawl_url

class crawl_attri(admin.ModelAdmin):
    class Meta:
        model=crawl_attribute
        
class crawl_css(admin.ModelAdmin):
    class Meta:
        model=final


class prod(admin.ModelAdmin):
    class Meta:
        model=cat
    #code

    
admin.site.register(website, SignUpAdmin)
admin.site.register(crawl_url,try_123) 	 	
admin.site.register(crawl_attribute,crawl_attri)
admin.site.register(final,crawl_css)
admin.site.register(cat,prod)