from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # tags
    path('',views.tags,name='tags'),
    path('<str:slug>/',views.tag,name='tag'),

]

