from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('', views.redirection, name = 'redirect'),
    path('PDSjoin/', views.PDSjoin),
    path('ADDIjoin/', views.ADDIjoin)
]