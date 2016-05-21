from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bonuri/', views.bonuri, name='home'),

]
