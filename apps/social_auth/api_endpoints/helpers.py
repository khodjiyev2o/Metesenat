from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User


def register_social_user(provider, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # create new user if it does not exist
        user = User.objects.create_user(email=email)
        user.auth_provider = provider
        user.save()

        return {"email": user.email, "tokens": user.tokens}

    if provider == user.auth_provider:
        # if already in db , just return token
        return {"email": user.email, "tokens": user.tokens}

    else:

        """This depends on the client's criteria, some want to authenticate user anyway,
        some want exactly the same provider to be used while authentication"""

        raise AuthenticationFailed(detail="Please continue your login using " + user.auth_provider)
