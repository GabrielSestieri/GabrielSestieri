from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'Home'
urlpatterns = [
    path('', views.index, name='index'),
]