from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'staffportal'
urlpatterns = [
    path('dashboard/', views.dash_post, name='dashboard'),
    path('submit_post/', views.submit_post, name='submit'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
