# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from . import views
urlpatterns = [
    # 折线图的url
    url(r'^linediagram/$', views.showlinediagram),
]