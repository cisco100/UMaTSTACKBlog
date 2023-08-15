from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import search,detail,category,home_view,feed_view
urlpatterns = [
    path('feed/',feed_view,name='feed',),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',home_view,name="home"),
    path('search/',search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('<slug:slug>/',category, name='category_detail'),
    

    ]