from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_inventory, name='home'),
    path('view/', views.view_inventory, name='viewBooks'),
    path('search/', views.search_inventory, name='searchBooks'),
]
