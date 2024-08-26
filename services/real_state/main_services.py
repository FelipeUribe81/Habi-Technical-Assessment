import json

from services.users.auth_services import check_is_authorized_user

from database import operations
from utils import constants, exceptions
from utils.exceptions import CustomUnauthorized, CustomBadRequest, CustomMethodNotAllowed


def get_properties(**kwargs):
    request_context = kwargs.get("request_context")
    headers = kwargs.get("headers")
    params = kwargs.get("query_params")

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
