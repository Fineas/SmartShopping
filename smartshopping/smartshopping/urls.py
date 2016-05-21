from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('magazin.urls')),
    url(r'^', include('authentication.urls')),
    url(r'^', include('home.urls')),
    url(r'^', include('bonuri.urls')),
    url(r'^', include('faq.urls')),
]
