from django.conf.urls import patterns, include, url
from first.views import my_view 
#from first.views import home
from first.views1 import search123

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^try_p/', 'try.views.home', name='my_view'),
     url(r'^blog/', my_view),
    #url(r'^blog1/', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^first/', search123),

)
