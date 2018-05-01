from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.hello_world, name='gateout_list'),
	url(r'^/data$', views.upload, name='upload_data'),
	url(r'^/image$', views.image, name='upload_data'),
]