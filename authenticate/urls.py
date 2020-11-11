from authenticate import views
from django.urls import path



urlpatterns = [
    path('', views.home, name="home"),
    path('Login/', views.user_login, name='Login'),
    path('Logout/',views.user_logout, name='Logout'),
    path('register/',views.user_registration, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('about_us/', views.about_us, name='about_us'),
 
 
]
