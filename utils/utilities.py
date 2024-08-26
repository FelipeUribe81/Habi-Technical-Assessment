import hashlib
from utils import constants


def encrypt_token(string_token):
    hashed_token = hashlib.sha256()
    hashed_token.update(string_token.encode('utf-8'))

    return hashed_token.hexdigest()


def clean_request_token(request_token):
    return request_token.replace(constants.TOKEN_PREFIX, "")
