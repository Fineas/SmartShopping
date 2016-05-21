from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/', views.register_page, name='register'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^reset/', views.reset_pass, name='reset'),

]