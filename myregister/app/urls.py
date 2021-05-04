
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('registration',views.registration),
    path('login/', views.login),
    path('home/', views.home)
    ]