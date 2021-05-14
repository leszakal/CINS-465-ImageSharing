"""image_host URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from posts import views as post_views
from posts.views import PostDetailed
from posts.views import PostUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('search/', core_views.search, name="search"),
    path('signup/', core_views.join, name="signup"),
    path('login/', core_views.user_login, name="login"),
    path('logout/', core_views.user_logout, name="logout"),
    path('upload/', post_views.new_upload, name="new_uploads"),
    path('user_uploads/', post_views.user_uploads, name="user_uploads"),
    path('posts/', post_views.browse_recent, name="browse_recent"),
    path('posts/<pk>/', PostDetailed.as_view(), name="post_detailed"),
    path('posts/<pk>/edit/', PostUpdateView.as_view(), name="post_update"),
    path('posts/<post_id>/delete/', post_views.delete_post, name="delete_post"),
    path('posts/<post_id>/comments/<comment_id>/delete/', post_views.delete_comment, name="delete_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
