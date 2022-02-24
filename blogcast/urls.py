from django.contrib import admin
from django.urls import path,include, re_path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('blogs/', include('blog.urls')),
 
    path('', views.index, name = "index" ),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    #path("podcast/", include('podcast.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)