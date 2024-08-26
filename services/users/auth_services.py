from utils.config import app_config
from utils.utilities import encrypt_token, clean_request_token


def check_is_authorized_user(request_token):
    """
       Return a boolean that indicates whether the request token is valid,
       thus validating user authorization.

       Attributes
       ----------
       request_token: str
           Token coming form the header request
      """

    app_secret = app_config.app_secret
    user = app_config.app_user
    password = app_config.app_password

    authorization_token = f"{app_secret}-{user}-{password}"
    hashed_token = encrypt_token(authorization_token)

    cleaned_request_token = clean_request_token(request_token)

    return cleaned_request_token == hashed_token
