from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import ContainerDetailView,ContainerListView
from django.views.decorators.csrf import csrf_exempt,csrf_protect

urlpatterns = [
    
    
    # url(r'/login^', views.Login, name='login'),
    url(r'^$', ContainerListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$',ContainerDetailView.as_view(),name='detail'),
    # url(r'^image/$', views.image, name='image'),
    # url(r'^data/$', views.upload, name='data'),

]