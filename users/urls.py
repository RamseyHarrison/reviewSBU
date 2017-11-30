from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [

    # ex: /register/
    url(r'^register/$', views.user_register, name='user_register'),

    # # ex: /login/
    # url(r'^login/$', views.user_login, name='user_login'),

    # ex: /accounts/...
    url(r'^accounts/', include('django.contrib.auth.urls')),

    # ex: /settings/
    url(r'^settings/$', views.user_settings, name='user_settings'),

    # ex: /profile/...
    url(r'^profile/(?P<userstring>[^/]+)/$', views.user_profile, name='user_profile'),

    # ex: /profile/juanathan/edit
    url(r'^profile/(?P<userstring>[^/]+)/edit/$', views.user_profile_edit, name='user_profile_edit'),

    # internal URL for user email confirmation
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),

    # internal URL for user email confirmation
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),
]
