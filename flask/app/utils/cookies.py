from flask import request
from app.errors import ForbiddenError
from app.constants import USER_COOKIE_KEY


def get_user_cookie(throw=None):
    """
    Parses user id cookie for a request

    @returns: user id for mongo doc if found else None
    """
    user_id = request.cookies.get(USER_COOKIE_KEY)
    if not user_id and throw:
        raise ForbiddenError()
    return user_id


def set_user_cookie(user_id):
    """
    Define callback to set the cookie headers for the response
    """

    def set_user_id(response):
        response.set_cookie(USER_COOKIE_KEY, user_id, httponly=False)
        return response

    return set_user_id