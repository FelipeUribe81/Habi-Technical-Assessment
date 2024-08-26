import json

from request_handler.request_handler import request_handler

if __name__ == '__main__':

    with open("data/sample_request.json") as file:
        request_event = json.load(file)

    try:
        properties = request_handler(request_event)
        print(json.dumps(properties, indent=4))
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        file.close()
