import json
import unittest

from request_handler.request_handler import request_handler


class TestFetchProperties(unittest.TestCase):

    def test_bad_request(self):
        with open("data/test_samples/sample_request_bad_request.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']

        self.assertEqual(status_code, 400)
        file.close()

    def test_authorization_bad_request(self):
        with open("data/test_samples/sample_request_missing_authorization_bad_request.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']

        self.assertEqual(status_code, 400)
        file.close()

    def test_invalid_authorization(self):
        with open("data/test_samples/sample_request_invalid_authorization.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']

        self.assertEqual(status_code, 401)
        file.close()

    def test_method_not_allowed(self):
        with open("data/test_samples/sample_request_method_not_allowed.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']

        self.assertEqual(status_code, 405)
        file.close()

    def test_valid_filters(self):
        with open("data/test_samples/sample_request_with_valid_filters.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertGreater(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()

    def test_no_filters(self):
        with open("data/test_samples/sample_request_no_filters.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertGreater(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()

    def test_invalid_status(self):
        with open("data/test_samples/sample_request_with_no_valid_status.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertEqual(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()

    def test_construction_year_filter(self):
        with open("data/test_samples/sample_request_construction_year_filter.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertGreater(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()

    def test_city_filter(self):
        with open("data/test_samples/sample_request_city_filter.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertGreater(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()

    def test_status_filter(self):
        with open("data/test_samples/sample_request_status_filter.json") as file:
            request_event = json.load(file)

        response = request_handler(request_event)
        status_code = response['statusCode']
        properties = json.loads(response['data']['properties'])

        self.assertGreater(len(properties), 0)
        self.assertEqual(status_code, 200)
        file.close()
