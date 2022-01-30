from django.urls import path

from . import views

app_name = 'frequency'
urlpatterns = [
    path('', views.frequency, name='frequency'),
]
