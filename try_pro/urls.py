from django.conf.urls import patterns, include, url
from first.views import my_view 
#from first.views import home
from first.views import search123
from first.views import add_details
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
     #url(r'^try_p/', 'try.views.home', name='my_view'),
     url(r'^blog/', my_view),
    #url(r'^blog1/', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^first/', search123),
    url(r'^details/', add_details),
    

)

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)