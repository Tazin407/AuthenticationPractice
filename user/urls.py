from django.urls import path, include
from .import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('change_pass/',views.change_pass_with_old, name='change_pass'),
    path('change_pass_easy/',views.change_pass_without_old, name='change_pass_easy'),
]