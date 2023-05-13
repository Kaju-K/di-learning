from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from .views import (
    SignUpView,
    profile_redirect_view,
    update_profile,
    create_profile,
    profile,
)

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile_redirect/", profile_redirect_view, name="profile_redirect"),
    path("profile_update/", update_profile, name="profile_update"),
    path("create_profile/", create_profile, name="create_profile"),
    path("profile/<int:profile_id>", profile, name="profile")
]