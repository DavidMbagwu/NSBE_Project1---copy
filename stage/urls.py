from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="stage-index"),
    path("about/", views.about, name="stage-about"),
    path("signup/", views.signup, name="stage-signup"),
    path("directory/", views.directory, name="stage-directory"),
    path("events/", views.events, name="stage-events"),
    path("help/", views.help, name="stage-help"),
    path("points/", views.points, name="stage-points"),
    path("profile/", views.profile, name="stage-profile"),
    path("login/", views.login_view, name="stage-login"),
    path("logout/", views.logout_view, name="stage-logout"),
    # Password reset views
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="stage/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="stage/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="stage/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="stage/password_reset_complete.html"), name="password_reset_complete"),
]
