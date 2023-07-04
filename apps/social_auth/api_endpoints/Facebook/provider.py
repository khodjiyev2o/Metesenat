import facebook


def validate(auth_token):
    """
    validate function queries the Facebook Graph API to fetch user info
    """
    try:
        graph = facebook.GraphAPI(access_token=auth_token)
        return graph.request("/me?fields=name,email")
    except:  # noqa
        return "The token is invalid or expired."
