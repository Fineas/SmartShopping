from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lant/$', views.creaza_lant, name='lant')
]
