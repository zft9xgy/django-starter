from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from personalweb import views
from django.contrib.sitemaps.views import sitemap
from personalweb import sitemaps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt',views.robots,name="robots"),
    path('', views.home,name='home'),
  
    # include
    path('notes/',include('notes.urls')),
    path('tags/',include('notes.tags.urls')),

    path('projects/',include('projects.urls')),
    path('pages/',include('pages.urls')),
    
    re_path(r'^filer/', include('filer.urls')),

    #django filer
    #path(r'^filer/', include('filer.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# sitemaps  
if settings.SEO_INDEX:
    urlpatterns += path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps.sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    


handler404 = 'personalweb.views.handler404'
handler500 = 'personalweb.views.handler500'

