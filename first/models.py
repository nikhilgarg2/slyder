from django.db import models
from django.utils.encoding import smart_unicode      
from django import forms

class text1(models.Model):
    class Meta:
        db_table='text1'
    text_ar=models.CharField(max_length=10)
    def __unicode__(self):
        return smart_unicode(self.text_ar)


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

    
class prodid(models.Model):
    class Meta:
        db_table='prodid'
    css_sel_id=models.CharField(max_length=100,unique=True)
    web_id=models.ForeignKey(website,db_column='web_id')
    text_ar=models.ForeignKey(text1,db_column='text_ar')
    attribute=models.CharField(max_length=100,null=True, blank=True)
    def __unicode__(self):
        return smart_unicode(self.css_sel_id)
    
    
class crawl_url_attribute_css_sel(models.Model):
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




class crawl_url_attribute_css_sel_value(models.Model):
    class Meta:
        db_table='crawl_url_attribute_css_sel_value'
    crawl_item_id=models.CharField(max_length=45)
    value=models.TextField()
    crawl_url_attribute_css_sel_id=models.ForeignKey(crawl_url_attribute_css_sel,db_column='crawl_url_attribute_css_sel_id')
    crawl_date=models.DateTimeField(auto_now_add=True)
    reconciled=models.BooleanField()
    reconciled_date=models.DateTimeField(auto_now_add=True)
    

        #code
    

