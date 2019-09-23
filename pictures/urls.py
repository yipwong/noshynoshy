from django.urls import path
from . import views

urlpatterns = [
    path('', views.pictures, {'id': ''}, name='home'),
    path('<str:id>/', views.pictures, name='showContent'),
]
