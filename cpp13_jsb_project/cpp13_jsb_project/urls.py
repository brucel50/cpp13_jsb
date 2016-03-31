from django.conf.urls import patterns, include, url
from django.contrib import admin
from homeapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpp13_jsb_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^homeapp/', include('homeapp.urls')),
    url(r'^$', views.index, name="index")

)
