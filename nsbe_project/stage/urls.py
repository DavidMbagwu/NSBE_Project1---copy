from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Serve static files when in DEBUG mode
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('home/', views.index, name='stage-index'),
    path('about/', views.about, name='stage-about'),
    path('signup/', views.signup, name='stage-signup'),
    path('directory/', views.directory, name='stage-directory'),
    path('events/', views.events, name='stage-events'),
    path('help/', views.help, name='stage-help'),
    path('points/', views.points, name='stage-points'),
    path('profile/', views.profile, name='stage-profile'),
    path('gallery/', views.gallery, name='stage-gallery'),
    path('', views.login_view, name='stage-login'),
    path('logout/', views.logout_view, name='stage-logout'),
    path('adminOnly/', views.adminOnly, name='stage-adminOnly'),

    # Password reset views
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
    path('password_reset_done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password_reset_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),

     path('events/', views.events, name='stage-events'),
     path('get-events/<str:event_type>/', views.get_events, name='stage-get-events'),
     path('get-event/<int:event_id>/', views.get_event, name='stage-get-event'),
     path('register/<int:event_id>/', views.register, name='stage-register'),
     path('unregister/<int:event_id>/', views.unregister, name='stage-unregister'),
]
