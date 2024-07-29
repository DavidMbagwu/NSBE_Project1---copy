from django.urls import path
from . import views

# Serve static files when in DEBUG mode
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='stage-index'),
    path('about/', views.about, name='stage-about'),
    path('signup/', views.signup, name='stage-signup'),
    path('directory/', views.directory, name='stage-directory'),
    path('events/', views.events, name='stage-events'),
    path('help/', views.help, name='stage-help'),
    path('points/', views.points, name='stage-points'),
    path('profile/', views.profile, name='stage-profile'),
    path('gallery/', views.gallery, name='stage-gallery'),
    path('login/', views.login_view, name='stage-login'),
    path('logout/', views.logout_view, name='stage-logout'),
    path('adminOnly/', views.adminOnly, name='stage-adminOnly'),
]
