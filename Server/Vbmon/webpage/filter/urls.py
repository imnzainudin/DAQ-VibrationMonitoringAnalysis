from django.urls import path

from . import views

app_name = 'filter'
urlpatterns = [
    path('', views.custom, name='custom'),
    path('filter:empty', views.empty, name='empty'),
]
