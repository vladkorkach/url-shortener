from django.conf.urls import url
from django.contrib import admin
from shorterurl import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name="home"),
    url(r'^shorterurl/$', views.shorter, name="shorterurl"),
    url(r'^(?P<input_url>[0-9a-zA-Z]+)/$', views.retrieve, name="reviewurl"),
]
