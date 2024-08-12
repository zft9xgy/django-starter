from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',views.userLogin,name='user-login'),
    path('register/',views.userRegister,name='user-register'),
    path('logout/',views.userLogout,name='user-logout'),
    path('account/',views.userAccount,name='user-account'),
    path('delete/',views.userDelete,name='user-delete'),

    # reset password
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
               template_name='users/pw-reset/users-reset-password.html',
               email_template_name='users/pw-reset/emails/users-reset-email.html',  # Plantilla de correo personalizada
               subject_template_name='users/pw-reset/emails/users-reset-subjet.txt',  # Plantilla opcional para el asunto del correo
               success_url=reverse_lazy('password_reset_done'),
          ), 
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/pw-reset/users-reset-password-done.html'), 
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/pw-reset/users-reset-password-confirm.html'), 
         name='password_reset_confirm'),
    
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='users/pw-reset/users-reset-password-complete.html'), 
         name='password_reset_complete'),
]
