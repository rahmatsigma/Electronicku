from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 

urlpatterns = [
    path('', LoginView.as_view(template_name='blog/login.html'), name='login'),        
    path('register/', views.register, name='register'),
    path('beranda/', views.beranda, name='beranda'),   
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]