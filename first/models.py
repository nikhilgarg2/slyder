from django.db import models
from django.utils.encoding import smart_unicode      
from django import forms

'''class text1(models.Model):
    class Meta:
        db_table='text1'
    text_ar=models.CharField(max_length=10)
    def __unicode__(self):
        return smart_unicode(self.text_ar)
'''

class website(models.Model):
    class Meta:
        db_table='website'     
    address=models.CharField(max_length=200,unique=True)
    frequency=models.IntegerField()
    active=models.BooleanField()   
    
    def __unicode__(self):
	return smart_unicode(self.address)



class crawl_url(models.Model):
    class Meta:
        db_table='crawl_url'
    website_id=models.ForeignKey(website,db_column='website_id')
    crawl_url=models.CharField(max_length=500)
    crawl_id=models.CharField(max_length=100, db_column='crawl_id')

    def __unicode__(self):
        return smart_unicode(self.crawl_id)

class crawl_attribute(models.Model):
    class Meta:
        db_table='crawl_attribute'
    name=models.CharField(max_length=100,unique=True)
    item_type=models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.name)

    
class cat(models.Model):
    class Meta:
        db_table='cat'
    category=models.CharField(max_length=45)
    
    def __unicode__(self):
        return smart_unicode(self.category)
    
    
'''class crawl_url_attribute_css_sel(models.Model):
    class Meta:
        db_table='crawl_url_attribute_css_sel'
    css_sel=models.CharField(max_length=100)
    crawl_attribute_id=models.ForeignKey(crawl_attribute,db_column='crawl_attribute_id')
    crawl_url_id=models.ForeignKey(crawl_url,db_column='crawl_url_id')
    text_ar=models.ForeignKey(text1,db_column='text_ar')
    status=models.BooleanField()
    last_crawled=models.DateTimeField(auto_now_add=True)
    prod_id=models.ForeignKey(prodid,db_column='prod_id')
    attribute=models.CharField(max_length=100, null=True, blank=True)   
    def __unicode__(self):
        return smart_unicode(self.css_sel)
'''

    
class scroll(models.Model):
    class Meta:
        db_table='scroll'
    click=models.BooleanField()
    click_id=models.CharField(max_length=45,unique=True,null=True, blank=True)
    scrape_before_click=models.BooleanField()
    web_id=models.ForeignKey(website,db_column='web_id')
        #code

class final(models.Model):
    class Meta:
        db_table='final'
    parent_css=models.CharField(max_length=45)
    prod_id=models.CharField(max_length=45)
    prod_attribute=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    mrp=models.CharField(max_length=45)
    sp=models.CharField(max_length=45)
    crawl_id=models.ForeignKey(crawl_url,db_column='crawl_id')
    cat=models.ForeignKey(cat,db_column='cat')
    
    def __unicode__(self):
        return smart_unicode(self.parent_css)
    #code

class dump_val(models.Model):
    class Meta:
        db_table='dump_val'
    crawl_item_id=models.CharField(max_length=45)
    name=models.TextField()
    mrp=models.CharField(max_length=20)
    sp=models.TextField(max_length=20)
    final_id=models.ForeignKey(final,db_column='final_id')
    crawl_date=models.DateTimeField(auto_now_add=True)
    reconciled=models.BooleanField()
    reconciled_date=models.DateTimeField(auto_now_add=True)
    
class item(models.Model):
    class Meta:
        db_table='item'
    name=models.CharField(max_length=100)
    category_id=models.ForeignKey(cat,db_column='category_id')

