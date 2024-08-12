from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/',views.userLogin,name='user-login'),
    path('register/',views.userRegister,name='user-register'),
    path('logout/',views.userLogout,name='user-logout'),
    path('account/',views.userAccount,name='user-account'),
    path('delete/',views.userDelete,name='user-delete'),
]
