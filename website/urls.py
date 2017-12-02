
from django.conf.urls import url, include

from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),

    url(r'^review/', views.reviewItem),

]