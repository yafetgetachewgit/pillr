from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^$', views.index, name='index'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^(?P<detail_level>[0-9]+)/$', views.timeline_detail, name='timeline_detail'),
]
