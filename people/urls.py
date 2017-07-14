from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^child/(?P<id>[0-9]+)?', views.view_child)
]