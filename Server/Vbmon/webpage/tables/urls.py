from django.urls import path

from . import views

app_name = 'tables'
urlpatterns = [
    path('', views.tables, name='tables'),
]
