from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/', TemplateView.as_view(template_name='layouts/about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='layouts/contact.html'), name='contact'),
]
