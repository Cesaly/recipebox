from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/', views.detail_recipe),
    path('author/<int:id>/', views.detail_author),
]
