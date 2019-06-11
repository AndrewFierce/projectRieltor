from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	url(r'^addinfo', views.addinfo, name='addinfo'),
	url(r'^addnewuser', views.addnewuser, name='addnewuser'),
	url(r'^changeinfo', views.changeinfo, name='changeinfo'),
	url(r'^typepremises', views.typepremises, name='typepremises'),
	url(r'^deleteimage', views.deleteimage, name='deleteimage'),
	url(r'^addimage', views.addimage, name='addimage'),
]