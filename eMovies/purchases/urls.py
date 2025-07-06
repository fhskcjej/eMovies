from django.contrib import admin
from django.urls import path, include
from purchases import views

urlpatterns = [
    path('complete/', views.purchase_complete, name='purchase_complete'),
    path('purchases/purchase_history/', views.purchase_history_view, name='purchase_history'),
]