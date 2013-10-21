from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import words.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#Simple Hello World
#    url(r'^$', 'website.views.home', name='home'), #home, simply 'domain.com'
   #words.views managed by app
   url(r'^$', words.views.ListWordView.as_view(), 
        name='word-list',),
   #create word, not practical atm
   url(r'^new$', words.views.CreateWordView.as_view(),
       name='word-new',),
   url(r'^parse$', words.views.ParseAddressView.as_view(),
       name='parse-address',),
   url(r'^display_parse$', words.views.DisplayParseView.as_view(),
       name='display-parse',),
    # Examples:
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
