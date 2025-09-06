from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'trade'  # Optional but useful for namespacing

urlpatterns = [
    path('', views.home, name='home'),  # Home page
     path('about-us/', views.about_us, name='about_us'),
    path('blogs/', views.blogs, name='blogs'),
    path('become-partner/', views.become_partner, name='become_partner'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),  # User registration

    
]