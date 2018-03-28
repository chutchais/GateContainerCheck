from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    # url(r'^', views.home, name='home'),
    
    # url(r'/login^', views.Login, name='login'),
    url(r'^image/', views.image, name='image'),
    url(r'^data/', views.upload, name='data'),

]