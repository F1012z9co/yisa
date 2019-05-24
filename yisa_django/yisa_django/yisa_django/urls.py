"""yisa_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
print(os.getcwd())
from django.conf.urls import url, include
from rest_framework import routers
from yisa_django.quickstart import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'daoju', views.DaojuViewSet)
router.register(r'shipin', views.ShipinViewSet)
router.register(r'wupin', views.WupinViewSet)
router.register(r'yaowan', views.YaowanViewSet)
router.register(r'chengjiu', views.ChengjiuViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', include('rest_framework.urls', namespace='rest_framework'))
]