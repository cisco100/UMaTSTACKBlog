from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap,CategorySiteMap
from blog.views import robots_txt
from blog.feeds import LatestPostsFeed
sitemaps={'post':PostSiteMap,'category':CategorySiteMap}
urlpatterns = [
    path('feed/atom/',LatestPostsFeed(),name="post_feed"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('auth/',include('authy.urls')),
    path('pdf/',include('pdf.urls')),
    path('',include('blog.urls')),
    path('robots.txt/', robots_txt, name='robots_txt'),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),



   
   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

