"""gatecontainercheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from customcheck.forms import LoginForm 
from .routers import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    
    url(r'^container/', include('customcheck.urls',namespace='container')),
    url(r'^gateout/', include('gateout.urls',namespace='gateout')),
    url(r'^', include('customcheck.urls')),
    url(r'^login/', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm} , name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/login'},name='logout'),
    url(r'^api/', include("customcheck.api.urls", namespace='container-api')),
    url(r'^api/gateout', include("gateout.api.urls", namespace='gateout-api')),
    url(r'^api2/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
