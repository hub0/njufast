from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
    path(
            'login/', 
            auth_views.LoginView.as_view(
                    template_name='core/login.html'
            ), 
            name='user_login'
    ),

    path(
            'logout/', 
            auth_views.LogoutView.as_view(
                    template_name='core/logout.html'
            ), 
            name='user_logout'
    ),

    path(
            'password-reset/', 
            auth_views.PasswordResetView.as_view(
                template_name='core/password_reset.html'
            ), 
            name='password_reset',
    ),

    path(
            'password-reset/done/', 
            auth_views.PasswordResetDoneView.as_view(
                template_name='core/password_reset_done.html'
            ), 
            name='password_reset_done',
    ),

    path(
            'password-reset-confirm/<uidb64>/<token>/', 
            auth_views.PasswordResetConfirmView.as_view(
                template_name='users/password_reset_confirm.html'
            ), 
            name='password_reset_confirm',
    ),

    path(
            'password-reset-complete/', 
            auth_views.PasswordResetCompleteView.as_view(
                template_name='users/password_reset_complete.html'
            ), 
            name='password_reset_complete',
    ),

    path('profile/', core_views.profile, name='user_profile'),
    
]
