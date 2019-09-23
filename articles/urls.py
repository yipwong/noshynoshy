from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, {'id': ''}, name='home'),
    path('<str:id>/', views.articles, name='showContent'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
]
# path('articles/<str:id>/', views.articles, name='ignore'),