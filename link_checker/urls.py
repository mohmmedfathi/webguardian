from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process_audio/', views.process_audio, name='process_audio'),
]