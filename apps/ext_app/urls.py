from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^show_dashboard$',views.show_dashboard),
    url(r'^travels/add/(?P<id>\d+)$',views.add_show),
    url(r'^create_list$',views.create_list),
    url(r'^show_travellist/(?P<id>\d+)$',views.show_travellist),
    url(r'^add_list/(?P<id>\d+)$',views.add_list),
]