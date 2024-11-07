from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('success/', views.signup_success, name='signup_success'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/',views.home_view,name="home")
]
