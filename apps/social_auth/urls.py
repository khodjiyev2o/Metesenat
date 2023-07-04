from django.urls import path
from apps.social_auth.api_endpoints import FacebookSocialAuthView


urlpatterns = [
    path("facebook/", FacebookSocialAuthView.as_view(), name="login-facebook"),
]