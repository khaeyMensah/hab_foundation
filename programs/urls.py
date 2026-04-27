from django.urls import path
from programs import views

urlpatterns = [
    path('', views.home, name='home'),
]