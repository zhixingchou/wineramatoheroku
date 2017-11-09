# coding: utf-8

"""winerama URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('registration.backends.default.urls')),   # 教程使用simple修改成default成功显示注册后的页面【安装django-registration-redux版本不同故障】
    url('^accounts/', include('django.contrib.auth.urls', namespace="auth")),   # 将 auth 应用中的 urls 模块包含进来
]
