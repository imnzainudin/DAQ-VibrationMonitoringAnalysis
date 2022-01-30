from django.urls import path

from . import views

app_name = 'live'
urlpatterns = [
    path('', views.live, name='live'),
]
