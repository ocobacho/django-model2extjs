from django.conf.urls import patterns, url, include

from rest_framework import routers

from . import views

urlpatterns = patterns('',
	#url(r'^', include(router.urls)),
	url(r'^$', views.index, name='ocgenerateextjs'),
	url(r'^mvc/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+)$', views.generate_mvc, name='mvc'),
	url(r'^files/model/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+).js$', views.download_model_file, name='app_model_file'),
	url(r'^files/store/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+).js$', views.download_store_file, name='app_store_file'),
	url(r'^files/controller/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+).js$', views.download_controller_file, name='app_controller_file'),
	url(r'^files/form/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+)form.js$', views.download_form_file, name='app_form_file'),
	url(r'^files/grid/(?P<appname>\w+)/(?P<module>\w+)/(?P<model>\w+)/list.js$', views.download_grid_file, name='app_grid_file'),
	url(r'^models/$', views.list_models, name='app_model'),

)