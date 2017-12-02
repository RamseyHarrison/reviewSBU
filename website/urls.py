
from django.conf.urls import url, include

from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD

    url(r'^review/', views.reviewItem),

]
=======
    url(r'^dining/(?P<dining_area>[a-z]+)$', views.dining, name='dining'),
    ]
>>>>>>> a6d7231a669f27c33bc0d1f8ebaee008cda8810e
