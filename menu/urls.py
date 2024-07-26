from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/clothing/top/', views.shop_top, name='clothing_top'),
]