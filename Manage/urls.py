from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage, name='manage'),
    path('food_supplier/', views.food_supplier, name='food_supplier'),
    path('foods/', views.foods, name='foods'),
]