from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('<str:slug>/',views.page,name='page'),
]
