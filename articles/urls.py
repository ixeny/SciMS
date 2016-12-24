from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^add', views.add, name='add'),
	url(r'^save', views.addArticle, name='addArticle'),
	url(r'^edit/(?P<id_art>[0-9]+)/$', views.edit, name='edit'),
	url(r'^notfound/$', views.notfound, name='notfound'),


	url(r'^(?P<id_art>[0-9]+)/$', views.getMLartcile, name='getMLartcile'),
	url(r'^read/(?P<id_art>[0-9]+)/$', views.readArticle, name='readArticle'),
	url(r'^view/(?P<id_art>[0-9]+)/$', views.viewArticle, name='viewArticle'),
	url(r'^delete/(?P<id_art>[0-9]+)/$', views.deleteArticle, name='deleteArticle'),

	url(r'^read', views.read, name='read'),

]

