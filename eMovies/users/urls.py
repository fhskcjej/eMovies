from django.contrib import admin
from django.urls import path, include
from users import views
from users.views import edit_profile_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('profile/card/', views.card_edit_view, name='card_edit'),
]