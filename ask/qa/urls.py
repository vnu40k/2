from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name='page'),
    url(r"^login/$", views.test, name='login'),
    url(r"^signup/$", views.test, name='signup'),
    url(r"^new/$", views.test, name='new'),
    url(r"^ask/.*$", views.ask, name='ask'),
    url(r"^popular/$", views.popular, name='popular'),
    url(r"^question/(?P<q_id>\d+)/$", views.question, name='question'),
]
