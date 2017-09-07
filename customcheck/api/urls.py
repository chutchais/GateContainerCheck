from django.conf.urls import url
from django.contrib import admin

from .views import (
   ContainerListAPIView,
   RejectListAPIView
    )

urlpatterns = [
	url(r'^container/$', ContainerListAPIView.as_view(), name='container_list'),
	url(r'^reject/$', RejectListAPIView.as_view(), name='container_list'),
	# url(r'^(?P<slug>[\w-]+)/$', VoyDetailAPIView.as_view(), name='voy_detail'),
 #    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]