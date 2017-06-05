from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^prescribe/', views.prescribe, name='prescribe'),
    url(r'^confirm/', views.pharma, name='pharma'),
]
