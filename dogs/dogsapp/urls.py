from django.urls import path

from . import views
from django.conf.urls import url
from dogsapp import views

urlpatterns = [
    url(r'^dogs/$', 
        views.DogsList.as_view(), 
        name=views.DogsList.name),
    url(r'^dogs/(?P<pk>[0-9]+)/$', 
        views.DogsDetail.as_view(),
        name=views.DogsDetail.name),
    url(r'^breeds/$', 
        views.BreedsList.as_view(),
        name=views.BreedsList.name),
    url(r'^breeds/(?P<pk>[0-9]+)/$', 
        views.BreedsDetail.as_view(),
        name=views.BreedsDetail.name),
    
]
