from django.conf.urls import  url
from coredrca import views

urlpatterns = [
	url(r'^artigo/(?P<ano>[0-9]{4})/$', views.artigo),
]
   

 