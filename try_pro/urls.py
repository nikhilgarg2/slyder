from django.conf.urls import patterns, include, url
from slyder.views import my_view 
#from first.views import home
from slyder.views import search123
from slyder.views import add_details
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from slyder.views import login1

urlpatterns = patterns('',
    # Examples:
     #url(r'^try_p/', 'try.views.home', name='my_view'),
     url(r'^home/', my_view),
    url(r'^$', login1),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', search123),
    url(r'^crawl/', add_details),
    

)

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
