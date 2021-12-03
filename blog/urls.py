from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('feexam/', views.feexam, name = 'blog-feexam'),
    path('quest/', views.quest, name = 'blog-quest'),
]
