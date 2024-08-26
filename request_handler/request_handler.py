import traceback
import json

from services.real_state import main_services

from utils.exceptions import CustomBadRequest, CustomUnauthorized, CustomMethodNotAllowed
from utils import constants


def request_handler(event):
    """
     To achieve handling the data from the client this function provides
     a way to catch the possible errors with the data incoming before
     to perform any service.

    Parameters
    ----------
    event : dict
        The sound the animal makes (default is None)

    Raises
    ------
    CustomBadRequest
        If the event object has an incomplete structure
    CustomMethodNotAllowed
        If the operation and http methods are not allowed by server
        configurations
    CustomUnauthorized
        If the user performing the action is not authorized
    """

    try:
        http_method = event.get("requestContext").get("httpMethod")

        if http_method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "*",
                    "Access-Control-Allow-Methods": "*"
                }
            }

        request_context = event.get("requestContext")
        headers = event.get("headers")
        query_params = event.get("queryStringParameters")
        path_parameters = event.get("pathParameters")
        operation = path_parameters.get("operation")

        if not headers:
            raise CustomBadRequest("Headers not found")

        return getattr(main_services, str(operation))(headers=headers, query_params=query_params,
                                                      request_context=request_context)

    except CustomBadRequest as e:
        return {
            "statusCode": 400,
            "headers": constants.REST_GENERAL_HEADERS,
            "data": json.dumps({"error": str(e)})
        }

    except CustomMethodNotAllowed as e:
        return {
            "statusCode": 405,
            "headers": constants.REST_GENERAL_HEADERS,
            "data": json.dumps({"error": str(e)})
        }

    except CustomUnauthorized as e:
        return {
            "statusCode": 401,
            "headers": constants.REST_GENERAL_HEADERS,
            "data": json.dumps({"error": str(e)})
        }

    except Exception as e:
        exception_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        print(exception_str)
        return {
            "statusCode": 500,
            "headers": constants.REST_GENERAL_HEADERS,
            "data": json.dumps({})
        }
