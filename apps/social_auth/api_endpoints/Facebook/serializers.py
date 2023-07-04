from rest_framework import serializers

from apps.social_auth.api_endpoints.Facebook.provider import validate
from apps.social_auth.api_endpoints.helpers import register_social_user


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = validate(auth_token)

        try:
            email = user_data["email"]
            provider = "facebook"
            return register_social_user(
                provider=provider,
                email=email,
            )
        except Exception:  # noqa

            raise serializers.ValidationError("The token  is invalid or expired. Please login again.")
