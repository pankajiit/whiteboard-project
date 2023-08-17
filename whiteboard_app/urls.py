from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views
from . import views

urlpatterns = [

    path('whiteboards/', views.whiteboard_list, name='whiteboard_list'),
    path('whiteboards/<int:whiteboard_id>/', views.whiteboard_detail, name='whiteboard_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('api/create_whiteboard/', views.create_whiteboard, name='create_whiteboard'),
    path('api/whiteboards/<int:whiteboard_id>/actions/', views.get_whiteboard_actions, name='get_whiteboard_actions'),
]
