import hashlib
from utils import constants


def encrypt_token(string_token):
    """
       To determine if a token is correct, this function encrypts a token so
       that it has the same structure as the token itself.

       Parameters
       ----------
       string_token: str
           Token with the correct structure that will be encrypted
    """

    hashed_token = hashlib.sha256()
    hashed_token.update(string_token.encode('utf-8'))

    return hashed_token.hexdigest()


def clean_request_token(request_token):
    """
       To perform the token comparison, the token coming from the client
       must be cleaned.

       Parameters
       ----------
       request_token: str
           Token that comes from the client's headers.
    """
    return request_token.replace(constants.TOKEN_PREFIX, "")
