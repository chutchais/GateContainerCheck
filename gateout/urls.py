from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import ContainerDetailView,ContainerListView,daily
from django.views.decorators.csrf import csrf_exempt,csrf_protect

urlpatterns = [
    url(r'^$', ContainerListView.as_view(), name='list'),
    url(r'^report/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',daily ,name='daily'),
    url(r'^(?P<slug>[-\w]+)/$',ContainerDetailView.as_view(),name='detail'),
    
]