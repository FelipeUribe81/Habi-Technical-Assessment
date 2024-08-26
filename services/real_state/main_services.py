import json

from services.users.auth_services import check_is_authorized_user

from database import operations
from utils import constants, exceptions
from utils.exceptions import CustomUnauthorized, CustomBadRequest, CustomMethodNotAllowed


def get_properties(**kwargs):
    """
    Check if data coming from server is suitable for the service purpose and
    retrieves the response object with properties data

    Parameters
    ----------
    Keyword Args:
        headers (dict): An object that describes headers coming from client
        query_params (dict): An object that contains optional search variables
        request_context (dict): An object that says the operations of request
    """

    headers = kwargs.get("headers")
    params = kwargs.get("query_params")
    request_context = kwargs.get("request_context")

    http_method = request_context.get("httpMethod")
    resource_path = request_context.get("resourcePath")

    if http_method != "GET":
        raise CustomMethodNotAllowed(f"Resource '{resource_path}' through method '{http_method}' not allowed")

    token = headers.get("Authorization")

    if not token:
        raise CustomBadRequest("Missing Authorization")

    is_authorized = check_is_authorized_user(token)

    if not is_authorized:
        raise CustomUnauthorized("User is not authorized")

    construction_year = params.get("construction_year")
    city = params.get("city")
    status = params.get("status")

    properties = operations.fetch_properties(construction_year, city, status)

    return {
        "statusCode": 200,
        "headers": constants.REST_GENERAL_HEADERS,
        "data": {
            "properties": json.dumps(properties)
        }
    }
