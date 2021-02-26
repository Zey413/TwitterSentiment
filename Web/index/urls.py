from django.urls import path
from django.views.generic import RedirectView

from . import views

#debug
from django.contrib import admin
from django.urls import path
#from MyWeb import views
# from django.conf.urls import url,include
#debug

urlpatterns = [
    path('', views.index),
    path('train/', views.train_feedback),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/index/images/favicon.ico')),


    #debug
    path('', admin.site.urls),
    path("grup/",views.grup,name = "grup"),
    #debug
    # url(r'^admin/', admin.site.urls),
    # # 定义图表url
    # url(r'^chart/', include('chart.urls'))
    path("showlinediagram/",views.showlinediagram,name = "showlinediagram"),
    #path('', chart.urls)
]
