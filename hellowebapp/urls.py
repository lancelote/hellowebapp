from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from django.views.generic import TemplateView, RedirectView

from collection.backends import MyRegistrationView

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
        r'^accounts',
        include('registration.backends.simple.urls')
    ),
    url(
        r'^accounts/create_thing/$',
        'collection.views.create_thing',
        name='registration_create_thing'
    ),
    url(
        r'^accounts/password/reset/$',
        password_reset,
        {
            'template_name': 'registration/password_reset_form.html'
        },
        name='password_reset'
    ),
    url(
        r'^accounts/password/reset/done/$',
        password_reset_done,
        {
            'template_name': 'registration/password_reset_done.html'
        },
        name='password_reset_done'
    ),
    url(
        r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {
            'template_name': 'registration/password_reset_confirm.html'
        },
        name='password_reset_confirm'
    ),
    url(
        r'^accounts/password/done/$',
        password_reset_complete,
        {
            'template_name': 'registration/password_reset_complete.html'
        },
        name='password_reset_complete'
    ),
    url(
        r'^accounts/register/$',
        MyRegistrationView.as_view(),
        name='registration_register'
    ),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^browse/',
        RedirectView.as_view(pattern_name='browse')
    ),
    url(
        r'^browse/name/$',
        'collection.views.browse_by_name',
        name='browse'
    ),
    url(
        r'^browse/name/(?P<initial>[-\w]+)/$',
        'collection.views.browse_by_name',
        name='browse_by_name'
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
        r'^thing/(?P<slug>[-\w]+)/edit/$',
        'collection.views.edit_thing',
        name='edit_thing'
    ),
    url(
        r'^things/$',
        RedirectView.as_view(pattern_name='browse')
    ),
]
