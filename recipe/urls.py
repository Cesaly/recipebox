from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd),
    path('<int:id>/', views.detail_recipe),
    path('author/<int:id>/', views.detail_author),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
]
