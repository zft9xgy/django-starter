from django.urls import path
from . import views

urlpatterns = [
    
    # notes
    path('',views.notes,name='notes'),
    path('<str:slug>/',views.note,name='note'),

]