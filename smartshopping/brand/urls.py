from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^brand/', views.brand, name='brand'),

]