from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^$',
        'collection.views.index',
        name='home'
    ),
    url(
        r'^about/',
        TemplateView.as_view(template_name='layouts/about.html'),
        name='about'
    ),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^contact/',
        TemplateView.as_view(template_name='layouts/contact.html'),
        name='contact'
    ),
    url(
        r'^thing/(?P<slug>[-\w]+)/$',
        'collection.views.thing_detail',
        name='thing_detail'
    ),
    url(
        r'thing/(?P<slug>[-\w]+)/edit/$',
        'collection.views.edit_thing',
        name='edit_thing'
    ),
]
